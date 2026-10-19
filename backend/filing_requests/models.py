from django.conf import settings
from django.db import models

from django.contrib.contenttypes.models import ContentType

from .choices import *


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    

class BaseRequest(models.Model):
    #User
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_requests"
    )

    #Request Options
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)

    #District
    district = models.ForeignKey(
        "District",
        on_delete=models.PROTECT
    )

    #range price
    min_price = models.BigIntegerField(blank=True, null=True)
    max_price = models.BigIntegerField(blank=True, null=True)

    #exact price
    exact_price = models.BigIntegerField(blank=True, null=True)

    #range area
    min_area = models.PositiveIntegerField(blank=True, null=True)
    max_area = models.PositiveIntegerField(blank=True, null=True)

    #exact area
    exact_area = models.PositiveIntegerField(blank=True, null=True)
    
    #meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def content_type_id(self):
        return ContentType.objects.get_for_model(self.__class__).id
    

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.get_user_type_display()} / {self.get_property_type_display()} - {self.district}"


class BuyApartmentRequest(BaseRequest):
    bedrooms = models.PositiveSmallIntegerField(choices=BEDROOM_CHOICES, default=1)
    year_built = models.SmallIntegerField(choices=YEAR_BUILT_CHOICES, blank=True, default=1)

    has_elevator = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_storage = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)


class SellApartmentRequest(BaseRequest):
    picture_1 = models.ImageField(upload_to="media/apartment/sell_apartment/", blank=True)
    picture_2 = models.ImageField(upload_to="media/apartment/sell_apartment/", blank=True)
    picture_3 = models.ImageField(upload_to="media/apartment/sell_apartment/", blank=True)
    picture_4 = models.ImageField(upload_to="media/apartment/sell_apartment/", blank=True)
    picture_5 = models.ImageField(upload_to="media/apartment/sell_apartment/", blank=True)
    address = models.CharField(max_length=150)
    bedrooms = models.PositiveSmallIntegerField(choices=BEDROOM_CHOICES, default=1)
    units_per_floor = models.PositiveSmallIntegerField(choices=UNITS_PER_FLOOR_CHOICES, default=1)
    floor = models.SmallIntegerField(choices=FLOOR_CHOICES, default=1)
    total_floors = models.PositiveSmallIntegerField(choices=TOTAL_FLOORS_CHOICES, default=1)
    year_built = models.SmallIntegerField(choices=YEAR_BUILT_CHOICES, default=1)

    has_elevator = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_storage = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)

    occupancy_status = models.SmallIntegerField(choices=OCCUPANCY_STATUS_CHOICES, default=1)
    deed_status = models.SmallIntegerField(choices=DEED_STATUS_CHOICES, default=1)

    description = models.CharField(max_length=500, blank=True)


class RentApartmentRequest(BaseRequest):
    bedrooms = models.PositiveSmallIntegerField(choices=BEDROOM_CHOICES, default=1)
    year_built = models.SmallIntegerField(choices=YEAR_BUILT_CHOICES, blank=True, default=1)

    min_deposit = models.BigIntegerField(null=True, blank=True)
    max_deposit = models.BigIntegerField(null=True, blank=True)
    min_monthly_rent = models.BigIntegerField(null=True, blank=True)
    max_monthly_rent = models.BigIntegerField(null=True, blank=True)

    has_elevator = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_storage = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)


class LeaseApartmentRequest(BaseRequest):
    picture_1 = models.ImageField(upload_to="media/apartment/lease_apartment", blank=True)
    picture_2 = models.ImageField(upload_to="media/apartment/lease_apartment", blank=True)
    picture_3 = models.ImageField(upload_to="media/apartment/lease_apartment", blank=True)
    picture_4 = models.ImageField(upload_to="media/apartment/lease_apartment", blank=True)
    picture_5 = models.ImageField(upload_to="media/apartment/lease_apartment", blank=True)

    address = models.CharField(max_length=150)
    bedrooms = models.PositiveSmallIntegerField(choices=BEDROOM_CHOICES, default=1)
    floor = models.SmallIntegerField(choices=FLOOR_CHOICES, default=1)
    total_floors = models.PositiveSmallIntegerField(choices=TOTAL_FLOORS_CHOICES, default=1)
    year_built = models.SmallIntegerField(choices=YEAR_BUILT_CHOICES, default=1)

    exact_deposit = models.BigIntegerField(null=True, blank=True)
    exact_monthly_rent = models.BigIntegerField(null=True, blank=True)
    is_convertible = models.BooleanField(default=False)

    min_deposit = models.BigIntegerField(null=True, blank=True)
    max_deposit = models.BigIntegerField(null=True, blank=True)
    min_monthly_rent = models.BigIntegerField(null=True, blank=True)
    max_monthly_rent = models.BigIntegerField(null=True, blank=True)

    occupancy_status = models.SmallIntegerField(choices=OCCUPANCY_STATUS_CHOICES, default=1)

    has_elevator = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_storage = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)
    