from django.urls import path
from .views import BuyApartmentCreateView, SellApartmentCreateView, RentApartmentCreateView, LeaseApartmentCreateView, BuyOfficeCreateView, SellOfficeCreateView, RentOfficeCreateView, LeaseOfficeCreateView, select_request_type, request_success
from . import views

app_name = "filing_requests"

urlpatterns = [
    path("", select_request_type, name="select_request_type"),
    path("request-success/", request_success, name="request_success"),
    # apartment urls
    path("buy-apartment/", BuyApartmentCreateView.as_view(), name="delete_later_buy_apartment"),
    path("sell-apartment/", SellApartmentCreateView.as_view(), name="delete_later_sell_apartment"),
    path("rent-apartment/", RentApartmentCreateView.as_view(), name="delete_later_rent_apartment"),
    path("lease-apartment/", LeaseApartmentCreateView.as_view(), name="delete_later_lease_apartment"),
    #office urls
    path("buy-office/", BuyOfficeCreateView.as_view(), name="buy_office"),
    path("sell-office/", SellOfficeCreateView.as_view(), name="sell_office"),
    path("rent-office/", RentOfficeCreateView.as_view(), name="rent_office"),
    path("lease-office/", LeaseOfficeCreateView.as_view(), name="lease_office"),

    #remove after the pages are built in frontend
    path("temp/buy-apartment/", views.buy_apartment_request, name="buy_apartment"),
    path("temp/sell-apartment/", views.sell_apartment_request, name="sell_apartment"),
    path("temp/rent-apartment/", views.rent_apartment_request, name="rent_apartment"),
    path("temp/lease-apartment/", views.lease_apartment_request, name="lease_apartment"),
]
