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
    (16, "۱۶"),
    (17, "۱۷"),
    (18, "۱۸"),
    (19, "۱۹"),
    (20, "۲۰+"),
]    

YEAR_BUILT_CHOICES = [
    ("0-5", "۰ تا ۵ سال"),
    ("5-10", "۵ تا ۱۰ سال"),
    ("10-15", "۱۰ تا ۱۵ سال"),
    ("15-20", "۱۵ تا ۲۰ سال"),
    ("20+", "بیش از ۲۰ سال"),
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
    bedrooms = models.PositiveSmallIntegerField(choices=BEDROOM_CHOICES)
    floor = models.SmallIntegerField(choices=FLOOR_CHOICES, blank=True)
    year_built = models.CharField(max_length=40, choices=YEAR_BUILT_CHOICES, blank=True)

    has_elevator = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_storage = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)


class SellApartmentRequest(BaseRequest):
    picture_1 = models.ImageField(upload_to="apartment_pictures/", blank=True)
    picture_2 = models.ImageField(upload_to="apartment_pictures/", blank=True)
    picture_3 = models.ImageField(upload_to="apartment_pictures/", blank=True)
    picture_4 = models.ImageField(upload_to="apartment_pictures/", blank=True)
    picture_5 = models.ImageField(upload_to="apartment_pictures/", blank=True)
    address = models.CharField(max_length=150)
    bedrooms = models.PositiveSmallIntegerField(choices=BEDROOM_CHOICES)
    units_per_floor = models.PositiveSmallIntegerField(choices=UNITS_PER_FLOOR_CHOICES)
    floor = models.SmallIntegerField(choices=FLOOR_CHOICES)

    has_elevator = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_storage = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)



    