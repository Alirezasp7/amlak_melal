from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.utils import timezone

from consultants.models import District


phone_number_validator = RegexValidator(
    regex=r'^09\d{9}$',
    message="شماره موبایل باید با ۰۹ شروع شود و دقیقا ۱۱ رقم باشد."
)


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            return ValueError("the phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user


    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11, unique=True, validators=[phone_number_validator], verbose_name="شماره تماس")
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_consultant = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number


class Consultant(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="consultant_profile"
    )

    avatar = models.ImageField(upload_to="consultants/avatar/", blank=True, null=True)
    districts = models.ManyToManyField(
        District,
        blank=True,
        related_name="consultants"
        )
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()}"
