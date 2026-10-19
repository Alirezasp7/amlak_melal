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

LISTING_TYPE_CHOICES = [
        ("sale", "فروش"),
        ("rent", "اجاره")
    ]