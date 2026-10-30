from django.urls import path

from .views import RequestOTPView, VerifyOTPView, PasswordLoginView, temp_login_view, temp_signup_view, temp_password_login_view

app_name = "accounts"

urlpatterns = [
    path('temp-login/', temp_login_view, name='temp_login'),
    path('temp-signup/', temp_signup_view, name='temp_signup'),
    path('temp-password-login/', temp_password_login_view, name='temp_password_login'),

    path("request-otp/", RequestOTPView.as_view(), name="request-otp"),
    path("verify-otp/", VerifyOTPView.as_view(), name="verify-otp"),
    path("login/", PasswordLoginView.as_view(), name="password-login"),
]