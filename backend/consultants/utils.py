from django.contrib.contenttypes.models import ContentType

from .models import Filing


from filing_requests.models import (
    BuyApartmentRequest, SellApartmentRequest,
    LeaseApartmentRequest, RentApartmentRequest
)

ALL_REQUEST_MODELS = [
    BuyApartmentRequest, SellApartmentRequest,
    LeaseApartmentRequest, RentApartmentRequest
]

def all_requests():
    result = []

    for model in ALL_REQUEST_MODELS:
        result.extend(
            model.objects.select_related("user", "district").all()
        )

    result.sort(key=lambda r: r.created_at, reverse=True)

    return result


def create_filing_from_request(req, user):
    """
    Create a draft Filing from a supply-side (seller/landlord) request.
    Copies the request's data into a new Filing and saves it.
    Does nothing if a Filing already exists for this (user, source request) pair.
    """

    # 1. Only supply-side requests produce filings
    if req.user_type not in ("seller", "landlord"):
        return None

    # 2. Determine the listing type
    if req.user_type == "seller":
        listing_type = "sale"
    else:
        listing_type = "rent"

    # 3. Check if a Filing already exists for this pair
    ct = ContentType.objects.get_for_model(req)

    already_exists = Filing.objects.filter(
        consultant=user,
        source_request_ct=ct,
        source_request_id=req.pk,
    ).exists()

    if already_exists:
        return None

    # 4. Build the Filing, copying fields from the request.
    #    getattr() is used for fields that may not exist on every request model.
    filing = Filing(
        consultant=user,
        source_request=req,
        property_type=req.property_type,
        listing_type=listing_type,
        district=req.district,

        # property details
        area=getattr(req, "exact_area", None),
        bedrooms=getattr(req, "bedrooms", None),
        floor=getattr(req, "floor", None),
        total_floors=getattr(req, "total_floors", None),
        units_per_floor=getattr(req, "units_per_floor", None),
        year_built=getattr(req, "year_built", ""),
        occupancy_status=getattr(req, "occupancy_status", ""),
        deed_status=getattr(req, "deed_status", ""),

        # features
        has_elevator=getattr(req, "has_elevator", False),
        has_parking=getattr(req, "has_parking", False),
        has_storage=getattr(req, "has_storage", False),
        has_balcony=getattr(req, "has_balcony", False),

        # content (consultant fills in later)
        title="",
        description="",

        # publishing state
        is_published=False,
        published_at=None,
    )

    # 5. Pricing — branch by user type
    if req.user_type == "seller":
        filing.price = getattr(req, "exact_price", None)

    elif req.user_type == "landlord":
        filing.deposit = getattr(req, "exact_deposit", None)
        filing.monthly_rent = getattr(req, "exact_monthly_rent", None)
        filing.is_convertible = getattr(req, "is_convertible", False)

        if filing.is_convertible:
            filing.min_deposit = getattr(req, "min_deposit", None)
            filing.max_deposit = getattr(req, "max_deposit", None)
            filing.min_rent = getattr(req, "min_monthly_rent", None)
            filing.max_rent = getattr(req, "max_monthly_rent", None)

    # 6. Save and return
    filing.save()
    return filing