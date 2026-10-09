from django.db import models
from django.conf import settings

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from filing_requests.choices import *
from filing_requests.models import District

# Create your models here.


class Listing(models.Model):
    #provenance
    consultant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="listings"
    )

    source_request_ct = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    source_request_id = models.PositiveIntegerField(null=True, blank=True)
    source_request = GenericForeignKey("source_request_ct", "source_request_id")

    #classification
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    listing_type = models.CharField(max_length=20, choices=LISTING_TYPE_CHOICES)

    #location
    district = models.ForeignKey(District, on_delete=models.PROTECT)
    address = models.CharField(max_length=200, blank=True)

    #property details
    area = models.PositiveIntegerField() 
    total_floors = models.PositiveSmallIntegerField(choices=TOTAL_FLOORS_CHOICES, null=True, blank=True)
    floor = models.SmallIntegerField(choices=FLOOR_CHOICES, null=True, blank=True)
    units_per_floor = models.PositiveSmallIntegerField(choices=UNITS_PER_FLOOR_CHOICES, null=True, blank=True)
    bedrooms = models.PositiveSmallIntegerField(choices=BEDROOM_CHOICES, null=True, blank=True)
    year_built = models.SmallIntegerField(choices=YEAR_BUILT_CHOICES, null=True, blank=True)
    occupancy_status = models.CharField(max_length=20, choices=OCCUPANCY_STATUS_CHOICES, blank=True)
    deed_status = models.CharField(max_length=20, choices=DEED_STATUS_CHOICES, blank=True)

    #pricing
    price = models.BigIntegerField(null=True, blank=True)
    deposit = models.BigIntegerField(null=True, blank=True)
    monthly_rent = models.BigIntegerField(null=True, blank=True)
    is_convertible = models.BooleanField(default=False)
    min_monthly_rent = models.BigIntegerField(null=True, blank=True)
    max_monthly_rent = models.BigIntegerField(null=True, blank=True)
    min_deposit = models.BigIntegerField(null=True, blank=True)
    max_deposit =models.BigIntegerField(null=True, blank=True)

    #features
    has_elevator = models.BooleanField(default=False)
    has_balcony = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    has_storage = models.BooleanField(default=False)

    #content
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    picture_1 = models.ImageField(upload_to="media/apartment",blank=True)
    picture_2 = models.ImageField(upload_to="media/apartment", blank=True)
    picture_3 = models.ImageField(upload_to="media/apartment", blank=True)
    picture_4 = models.ImageField(upload_to="media/apartment", blank=True)
    picture_5 = models.ImageField(upload_to="media/apartment", blank=True)

    #publishing
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return f"{self.title} ({self.get_listing_type_display()})"
    



