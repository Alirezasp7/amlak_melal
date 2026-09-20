from django.conf import settings
from django.db import models

from .request_options import USER_TYPE_CHOICES, PROPERTY_TYPE_CHOICES


BEDROOM_CHOICES = [
    (1, "۱"),
    (2, "۲"),
    (3, "۳"),
    (4, "۴"),
    (5, "۵+"),
]

FLOOR_CHOICES = [
    (-1, "زیرزمین"),
    (0, "همکف"),
    (1, "۱"),
    (2, "۲"),
    (3, "۳"),
    (4, "۴"),
    (5, "۵"),
    (6, "۶"),
    (7, "۷"),
    (8, "۸"),
    (9, "۹"),
    (10, "۱۰"),
    (11, "۱۱"),
    (12, "۱۲"),
    (13, "۱۳"),
    (14, "۱۴"),
    (15, "۱۵"),
]

TOTAL_FLOORS_CHOICES = [
    (1, "۱"),
    (2, "۲"),
    (3, "۳"),
    (4, "۴"),
    (5, "۵"),
    (6, "۶"),
    (7, "۷"),
    (8, "۸"),
    (9, "۹"),
    (10, "۱۰"),
    (11, "۱۱"),
    (12, "۱۲"),
    (13, "۱۳"),
    (14, "۱۴"),
    (15, "۱۵"),
]

YEAR_BUILT_CHOICES = [
    (0, "نوساز"),
    (1, "۱"),
    (2, "۲"),
    (3, "۳"),
    (4, "۴"),
    (5, "۵"),
    (6, "۶"),
    (7, "۷"),
    (8, "۸"),
    (9, "۹"),
    (10, "۱۰"),
    (11, "۱۱"),
    (12, "۱۲"),
    (13, "۱۳"),
    (14, "۱۴"),
    (15, "۱۵"),
    (16, "۱۶"),
    (17, "۱۷"),
    (18, "۱۸"),
    (19, "۱۹"),
    (20, "۲۰"),
    (21, "۲۱"),
    (22, "۲۲"),
    (23, "۲۳"),
    (24, "۲۴"),
    (25, "۲۵"),
    (26, "۲۶"),
    (27, "۲۷"),
    (28, "۲۸"),
    (29, "۲۹"),
    (30, "۳۰+"),
]

UNITS_PER_FLOOR_CHOICES = [
    (1, "۱"),
    (2, "۲"),
    (3, "۳"),
    (4, "۴"),
    (5, "۵"),
    (6, "۶"),
    (7, "۷"),
    (8, "۸"),
    (9, "۹"),
    (10, "۱۰")
]

OCCUPANCY_STATUS_CHOICES = [
    (1, "سکونت مالک"),
    (2, "سکونت مستاجر"),
    (3, "تخلیه")
]

DEED_STATUS_CHOICES = [
    (1, "تک برگ"),
    (2, "دفترچه ای"),
    (3, "قولنامه ای"),
    (4, "اوقاف"),
    (5, "تعاونی"),
    (6, "در دست اقدام")
]


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
    picture_5 = models.ImageField(upload_to="amedia/apartment/sell_apartment/", blank=True)
    address = models.CharField(max_length=150)
    bedrooms = models.PositiveSmallIntegerField(choices=BEDROOM_CHOICES, default=1)
    units_per_floor = models.PositiveSmallIntegerField(choices=UNITS_PER_FLOOR_CHOICES, default=1)
    floor = models.SmallIntegerField(choices=FLOOR_CHOICES, default=1)
    total_floors = models.SmallIntegerField(choices=TOTAL_FLOORS_CHOICES, default=1)
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
    total_floors = models.SmallIntegerField(choices=TOTAL_FLOORS_CHOICES, default=1)
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
    