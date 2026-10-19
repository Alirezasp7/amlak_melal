from django import forms
from filing_requests.forms import _validate_range
from .models import Filing


class ApartmentSaleFilingForm(forms.ModelForm):
    class Meta:
        model = Filing
        fields = [
            "picture_1",
            "picture_2",
            "picture_3",
            "picture_4",
            "picture_5",
            "title",
            "district",
            "area",
            "price",
            "bedrooms",
            "floor",
            "total_floors",
            "units_per_floor",
            "year_built",
            "occupancy_status",
            "deed_status",
            "has_elevator", "has_storage", "has_balcony", "has_parking",
            "description"
        ]


class ApartmentLeaseFilingForm(forms.ModelForm):
    class Meta:
        model = Filing
        fields = [
            "picture_1",
            "picture_2",
            "picture_3",
            "picture_4",
            "picture_5",
            "district",
            "area",
            "bedrooms",
            "floor",
            "year_built",
            "exact_deposit", "exact_monthly_rent",
            "min_deposit", "max_deposit", "min_monthly_rent", "max_monthly_rent",
            "is_convertible",
            "has_elevator", "has_parking", "has_storage", "has_balcony",
            "description"
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


FILING_FORM_MAP = {
    ("apartment", "sale"): ApartmentSaleFilingForm,
    ("apartment", "rent"): ApartmentLeaseFilingForm,
    # ("old", "sale"): OldSaleFilingForm,
    # ("commercial", "sale"): CommercialSaleFilingForm,
    # ("commercial", "rent"): CommercialRentFilingForm,
    # ("office", "sale"): OfficeSaleFilingForm,
    # ("office", "rent"): OfficeRentFilingForm,
}