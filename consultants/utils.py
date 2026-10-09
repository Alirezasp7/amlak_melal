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
