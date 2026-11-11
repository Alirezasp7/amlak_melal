from rest_framework import serializers
from .models import BuyApartmentRequest, SellApartmentRequest, RentApartmentRequest, LeaseApartmentRequest, BuyOfficeRequest, SellOfficeRequest, RentOfficeRequest, LeaseOfficeRequest
from .utils import validate_range


class BuyApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        Model = BuyApartmentRequest
        fields = [
            "district",
            "min_price", "max_price",
            "min_area", "max_area",
            "bedrooms",
            "year_built",
            "has_elevator", "has_storage", "has_balcony", "has_parking"
        ]

        def validate(self, data):
            errors = {}

            validate_range(data, errors, "min_price", "max_price", "قیمت")
            validate_range(data, errors, "min_area", "max_area", "متراژ")

            if errors:
                raise serializers.ValidationError(errors)

            return data


class SellApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellApartmentRequest
        fields = [
            "picture_1",
            "picture_2",
            "picture_3",
            "picture_4",
            "picture_5",
            "district",
            "address",
            "exact_area",
            "bedrooms",
            "year_built",
            "units_per_floor",
            "floor",
            "total_floors",
            "exact_price",
            "occupancy_status",
            "deed_status",
            "has_elevator", "has_storage", "has_balcony", "has_parking",
            "description"
        ]

      
class RentApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentApartmentRequest      
        fields = [
            "district",
            "min_area",
            "max_area",
            "bedrooms",
            "year_built",
            "min_deposit",
            "max_deposit",
            "min_monthly_rent",
            "max_monthly_rent",
            "has_elevator", "has_parking", "has_storage", "has_balcony"
        ]

        def validate(self, data):
            errors = {}

            validate_range(data, errors, "min_monthly_rent", "max_monthly_rent", "اجاره ماهانه")
            validate_range(data, errors, "min_deposit", "max_deposit", "رهن")
            validate_range(data, errors, "min_area", "max_area", "متراژ")

            if errors:
                raise serializers.ValidationError(errors)

            return data


class LeaseApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaseApartmentRequest
        fields = [
            "picture_1",
            "picture_2",
            "picture_3",
            "picture_4",
            "picture_5",
            "district",
            "address",
            "exact_area",
            "bedrooms",
            "floor",
            "year_built",
            "exact_deposit", "exact_monthly_rent",
            "min_deposit", "max_deposit", "min_monthly_rent", "max_monthly_rent",
            "is_convertible",
            "has_elevator", "has_parking", "has_storage", "has_balcony"
        ]

        def validate(self, data):
            errors = {}

            validate_range(data, errors, "min_monthly_rent", "max_monthly_rent", "اجاره ماهانه")
            validate_range(data, errors, "min_deposit", "max_deposit", "رهن")

            if errors:
                raise serializers.ValidationError(errors)

            return data


class BuyOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyOfficeRequest
        fields = [
            "district",
            "min_price", "max_price",
            "min_area", "max_area",
            "rooms",
            "year_built",
            "deed_status",
            "has_elevator", "has_storage", "has_parking"
        ]

        def validate(self, data):
            errors = {}

            validate_range(data, errors, "min_price", "max_price", "قیمت")
            validate_range(data, errors, "min_area", "max_area", "متراژ")

            if errors:
                raise serializers.ValidationError(errors)

            return data


class SellOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellOfficeRequest
        fields = [
            "picture_1",
            "picture_2",
            "picture_3",
            "picture_4",
            "picture_5",
            "district",
            "address",
            "exact_area",
            "rooms",
            "year_built",
            "units_per_floor",
            "floor",
            "total_floors",
            "exact_price",
            "deed_status",
            "has_elevator", "has_storage", "has_parking",
            "description"
        ]


class RentOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentOfficeRequest
        fields = [
            "district",
            "min_area",
            "max_area",
            "rooms",
            "year_built",
            "min_deposit",
            "max_deposit",
            "min_monthly_rent",
            "max_monthly_rent",
            "has_elevator", "has_parking", "has_storage",
            "deed_status"
        ]

        def validate(self, data):
            errors = {}

            validate_range(data, errors, "min_monthly_rent", "max_monthly_rent", "اجاره ماهانه")
            validate_range(data, errors, "min_deposit", "max_deposit", "رهن")
            validate_range(data, errors, "min_area", "max_area", "متراژ")

            if errors:
                raise serializers.ValidationError(errors)

            return data


class LeaseOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaseOfficeRequest
        fields = [  
            "picture_1",
            "picture_2",
            "picture_3",
            "picture_4",
            "picture_5",
            "district",
            "address",
            "exact_area",
            "rooms",
            "floor",
            "year_built",
            "exact_deposit", "exact_monthly_rent",
            "min_deposit", "max_deposit", "min_monthly_rent", "max_monthly_rent",
            "is_convertible",
            "deed_status",
            "has_elevator", "has_parking", "has_storage",
            "description"
        ]

        def validate(self, data):
            errors = {}

            validate_range(data, errors, "min_monthly_rent", "max_monthly_rent", "اجاره ماهانه")
            validate_range(data, errors, "min_deposit", "max_deposit", "رهن")

            if errors:
                raise serializers.ValidationError(errors)

            return data
