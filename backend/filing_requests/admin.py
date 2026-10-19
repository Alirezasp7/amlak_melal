from django.contrib import admin
from .models import District, BuyApartmentRequest


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(BuyApartmentRequest)
class BuyApartmentRequestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "user_type",
        "property_type",
        "district",
        "created_at",
    )
    list_filter = ("user_type", "property_type", "district")