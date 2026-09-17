from django.urls import path
from . import views

app_name = "filing_requests"

urlpatterns = [
    path("", views.select_request_type, name="select_request_type"),
    path("buy-apartment/", views.buy_apartment_request, name="buy_apartment"),
    path("request-success/", views.request_success, name="request_success"),
]