from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import generate_otp, verify_otp

from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def temp_login_view(request):
    if request.method == "POST":
        step = request.POST.get("step")
        phone = request.POST.get("phone_number")
        
        if step == "request_otp":
            # 1. User submitted phone number
            generate_otp(phone)
            return render(request, "temp_login.html", {"phone": phone, "step": "verify"})
            
        elif step == "verify_otp":
            # 2. User submitted the OTP code
            code = request.POST.get("code")
            if verify_otp(phone, code):
                user, created = User.objects.get_or_create(phone_number=phone)
                # Log them into the Django session just for this test
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return render(request, "temp_success.html", {"user": user, "created": created})
            else:
                return render(request, "temp_login.html", {"phone": phone, "step": "verify", "error": "Invalid code"})
                
    # Initial page load (GET)
    return render(request, "temp_login.html", {"step": "request"})


def temp_signup_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone_number")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        # Check if user already exists
        if User.objects.filter(phone_number=phone).exists():
            return render(request, "temp_signup.html", {"error": "این شماره قبلا ثبت نام کرده است."})

        # Create the new user with a password
        user = User.objects.create_user(
            phone_number=phone, 
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        # Log them in automatically
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        
        return render(request, "temp_success.html", {"user": user, "created": True})

    return render(request, "temp_signup.html")


def temp_password_login_view(request):
    if request.method == "POST":
        phone = request.POST.get("phone_number")
        password = request.POST.get("password")

        try:
            user = User.objects.get(phone_number=phone)
            if user.check_password(password):
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return render(request, "temp_success.html", {"user": user, "created": False})
            else:
                return render(request, "temp_password_login.html", {"error": "رمز عبور اشتباه است."})
        except User.DoesNotExist:
            return render(request, "temp_password_login.html", {"error": "کاربری با این شماره یافت نشد."})

    return render(request, "temp_password_login.html")


User = get_user_model()


class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = request.data.get("phone_number")
        password = request.data.get("password")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if not all([phone, password, first_name, last_name]):
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if not phone or len(phone) != 11 or not phone.startswith("09"):
            return Response({"error": "this phone number is invalid"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            dummy_user = User(phone_number=phone, first_name=first_name, last_name=last_name)

            validate_password(password=password, user=dummy_user)

        except ValidationError as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(phone_number=phone).exists():
            return Response({"error": "This phone number already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            phone_number= phone,
            password= password,
            first_name= first_name,
            last_name= last_name
        )

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=status.HTTP_201_CREATED)

class RequestOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = request.data.get("phone_number")

        if not phone:
            return Response({"error":"phone number is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not User.objects.filter(phone_number=phone).exists():
            return Response({"error": "this phone number is not registered. please signup first."}, status=status.HTTP_404_NOT_FOUND)

        generate_otp(phone)

        return Response({"message":"OTP sent successfully"}, status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = request.data.get("phone_number")
        code = request.data.get("code")

        if not verify_otp(phone, code):
            return Response({"error":"invalid or expired code"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get_or_create(phone_number=phone)

        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }, status=status.HTTP_200_OK)


class PasswordLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        phone = request.data.get("phone_number")
        password = request.data.get("password")

        try:
            user = User.objects.get(phone_number=phone)

            if user.check_password(password):
                refresh = RefreshToken.for_user(user)

                return Response({
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }, status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            pass

        return Response({"error": "Invalid phone or password"}, status=status.HTTP_401_UNAUTHORIZED)