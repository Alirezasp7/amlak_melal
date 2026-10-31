from rest_framework import serializers
from consultants.models import Filing

class PublicFilingSerializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source="district.name", read_only=True)

    consultant_name = serializers.CharField(source="consultant.user.get_full_name", read_only=True)
    consultant_phone_number = serializers.CharField(source="consultant.user.phone_number", read_only=True)
    consultant_avatar = serializers.ImageField(source="consultant.avatar", read_only=True)

    property_type_display = serializers.CharField(source="get_property_type_display", read_only=True)
    listing_type_display = serializers.CharField(source="get_listing_type_display", read_only=True)

    bedrooms_display = serializers.CharField(source="get_bedrooms_display", read_only=True)
    floor_display = serializers.CharField(source="get_floor_display", read_only=True)
    total_floors_display = serializers.CharField(source="get_total_floors_display", read_only=True)
    year_built_display = serializers.CharField(source="get_year_built_display", read_only=True)
    units_per_floor_display = serializers.CharField(source="get_units_per_floor_display", read_only=True)
    occupancy_status_display = serializers.CharField(source="get_occupancy_status_display", read_only=True)
    deed_status_display = serializers.CharField(source="get_deed_status_display", read_only=True)

    class Meta:
        model = Filing
        fields = [
            'id', 'title', 'description', 
            
            # Types
            'property_type', 'property_type_display',
            'listing_type', 'listing_type_display',
            
            # Location
            'district_name',
            
            # Property details
            'area', 
            'total_floors', 'total_floors_display',
            'floor', 'floor_display',
            'units_per_floor', 'units_per_floor_display',
            'bedrooms', 'bedrooms_display',
            'year_built', 'year_built_display',
            'occupancy_status', 'occupancy_status_display',
            'deed_status', 'deed_status_display',
            
            # Pricing 
            'price', 
            'exact_deposit', 'exact_monthly_rent', 
            'is_convertible',
            'min_deposit', 'max_deposit',
            'min_monthly_rent', 'max_monthly_rent',
            
            # Features
            'has_elevator', 'has_balcony', 'has_parking', 'has_storage',
            
            # Images
            'picture_1', 'picture_2', 'picture_3', 'picture_4', 'picture_5',
            
            # Consultant
            'consultant_name', 'consultant_phone_number', 'consultant_avatar',
            
            # Meta
            'created_at', 'published_at', 'is_published'
        ]