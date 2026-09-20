from django import forms
from .request_options import USER_TYPE_CHOICES, PROPERTY_TYPE_CHOICES, EXCLUDED_PROPERTY_TYPES
from .models import BuyApartmentRequest, SellApartmentRequest, RentApartmentRequest, LeaseApartmentRequest

class RequestSelectionForm(forms.Form):
    """
    One-page selection: نوع کاربر + نوع ملک.
    All property type choices are included here (so Django doesn't reject a
    valid submission) — the browser hides کلنگی for مستاجر/موجر via JS, and
    clean() double-checks the combination server-side too.
    """

    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        label="نوع کاربر",
        widget=forms.Select(attrs={"class": "form-select", "id": "id_request_type"}),
    )
    property_type = forms.ChoiceField(
        choices=PROPERTY_TYPE_CHOICES,
        label="نوع ملک",
        widget=forms.Select(attrs={"class": "form-select", "id": "id_property_type"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get("user_type")
        property_type = cleaned_data.get("property_type")

        if user_type and property_type:
            excluded = EXCLUDED_PROPERTY_TYPES.get(user_type, [])
            if property_type in excluded:
                self.add_error(
                    "property_type",
                    "این نوع ملک برای این نوع کاربر قابل انتخاب نیست.",
                )
        return cleaned_data


class BuyApartmentRequestForm(forms.ModelForm):
    class Meta:
        model = BuyApartmentRequest
        fields = [
            "district",
            "min_price", "max_price",
            "min_area", "max_area",
            "bedrooms",
            "year_built",
            "has_elevator", "has_storage", "has_balcony", "has_parking"
            ]
        

    def clean(self):
        cleaned_data = super().clean()

        _validate_range(self, cleaned_data, "min_price", "max_price", "قیمت")
        _validate_range(self, cleaned_data, "min_area", "max_area", "متراژ")

        return cleaned_data

    
class SellApartmentRequestForm(forms.ModelForm):
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


class RentApartmentRequestForm(forms.ModelForm):
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


    def clean(self):
        cleaned_data = super().clean()

        _validate_range(self, cleaned_data, "min_area", "max_area", "متراژ")

        return cleaned_data


class LeaseApartmentRequestForm(forms.ModelForm):
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

    
    def clean(self):
        cleaned_data = super().clean()
        convertible = cleaned_data.get("is_convirtible")

        range_fields = ["min_deposit", "max_deposit", "min_monthly_rent", "max_monthly_rent"]
        exact_fields = ["exact_deposit", "exact_monthly_rent"]

        if convertible:
            for field in range_fields:
                if cleaned_data.get(field) is None:
                    self.add_error(field, "این فیلد در حالت قابل تبدیل الزامی است")
        
            for field in exact_fields:
                if cleaned_data.get(field) is not None:
                    self.add_error(field, "در حالت قابل تبدیل نباید مقدار دقیق وارد شود")
            
            _validate_range(self, cleaned_data, "min_deposit", "max_deposit", "رهن")
            _validate_range(self, cleaned_data, "min_monthly_rent", "max_monthly_range", "اجاره ماهانه")
        else:
            for field in range_fields:
                if cleaned_data.get(field):
                    self.add_error(field, "در حالت غیر قابل تبدیل نباید بازه وارد شود")
            
            for field in exact_fields:
                if cleaned_data.get(field):
                    self.add_error(field, "این فیلد الزامی است")
        
        return cleaned_data


def _validate_range(form, cleaned_data, min_field, max_field, label):
        min_value = cleaned_data.get(min_field)
        max_value = cleaned_data.get(max_field) 

        if min_value is not None and max_value is not None and min_value > max_value:
            form.add_error(
                max_field,
                f"{label}: مقدار حداکثر باید بزرگ‌تر یا مساوی حداقل باشد."
            )