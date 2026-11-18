from django.db import models
from django.conf import settings

from consultants.models import Filing

# Create your models here.


class Favorites(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favortes"
    )

    filing = models.ForeignKey(Filing, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
