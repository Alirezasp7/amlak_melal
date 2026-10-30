import random
from django.core.cache import cache

def generate_otp(phone_number):
    code = str(random.randint(10000, 99999))

    cache.set(f"otp_{phone_number}", code, timeout=120)

    #integrate kevenegar/sms.ir 
    print(f"sms to {phone_number}: your login code is {code}")

    return code


def verify_otp(phone_number, code):
    saved_code = cache.get(f"otp_{phone_number}")

    if saved_code and saved_code == code:
        cache.delete(f"otp_{phone_number}")
        return True
    
    return False