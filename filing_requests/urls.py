from django.urls import path
from . import views

app_name = "filing_requests"

urlpatterns = [
    path("", views.select_request_type, name="select_request_type"),
    path("request-success/", views.request_success, name="request_success"),
    path("buy-apartment/", views.buy_apartment_request, name="buy_apartment"),
    path("sell-apartment/", views.sell_apartment_request, name="sell_apartment"),
    path("rent-apartment/", views.rent_apartment_request, name="rent_apartment")
]