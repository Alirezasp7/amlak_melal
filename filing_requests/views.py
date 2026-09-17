from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import RequestSelectionForm, BuyApartmentRequestForm
from .request_options import USER_TYPE_CHOICES, PROPERTY_TYPE_CHOICES, EXCLUDED_PROPERTY_TYPES, BUYER, SELLER, TENANT, LANDLORD, APARTMENT, COMMERCIAL, OFFICE, KOLANGI


REQUEST_TYPE_LABELS = dict(USER_TYPE_CHOICES)
PROPERTY_TYPE_LABELS = dict(PROPERTY_TYPE_CHOICES)


@login_required
def select_request_type(request):
    """
    One page: pick نوع کاربر and نوع ملک together.
    کلنگی is hidden client-side (JS) when the user type is مستاجر/موجر,
    and rejected server-side too if someone bypasses the JS.
    """
    if request.method == "POST":
        form = RequestSelectionForm(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data["user_type"]
            property_type = form.cleaned_data["property_type"]

            if user_type == "buyer" and property_type == "apartment":
                return redirect("filing_requests:buy_apartment")
            else:
                form = RequestSelectionForm()
    else:
        form = RequestSelectionForm()

    return render(
        request,
        "filing_requests/select_type.html",
        {
            "form": form,
            "excluded_map": EXCLUDED_PROPERTY_TYPES,
        },
    )


@login_required
def buy_apartment_request(request):
    if request.method == "POST":
        form = BuyApartmentRequestForm(request.POST)
        
        if form.is_valid():
            apartment_request = form.save(commit= False)
            apartment_request.user = request.user
            apartment_request.user_type = BUYER
            apartment_request.property_type = APARTMENT
            apartment_request.save() 

            return redirect("filing_requests:request_success")

    else:
        form = BuyApartmentRequestForm()

    return render(request, "filing_requests/buy_apartment.html", {"form": form})


def request_success(request):
    return render(request, "filing_requests/request_success.html")