#User Type
SELLER = "seller"
BUYER = "buyer"
TENANT = "tenant"
LANDLORD = "landlord"

USER_TYPE_CHOICES = [
    (SELLER, "فروشنده"),
    (BUYER, "خریدار"),
    (TENANT, "مستاجر"),
    (LANDLORD, "موجر")
]


#Property Type

APARTMENT = "apartment"
COMMERCIAL = "commercial"
OFFICE = "office"
KOLANGI = "kolangi"

PROPERTY_TYPE_CHOICES = [
    (APARTMENT, "آپارتمان"),
    (COMMERCIAL, "تجاری"),
    (OFFICE, "اداری"),
    (KOLANGI, "کلنگی")
]

#Exluded Property Types
EXCLUDED_PROPERTY_TYPES = {
    TENANT: [KOLANGI],
    LANDLORD: [KOLANGI]
}

def property_type_choices_for(user_type):
    excluded = EXCLUDED_PROPERTY_TYPES.get(user_type, [])

    result = []
    for value, lable in PROPERTY_TYPE_CHOICES:
        if value not in excluded:
            result.append((value, lable))
    return result