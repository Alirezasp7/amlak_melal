from django.contrib import admin

from .models import Favorite
# Register your models here.

@admin.register(Favorite)
class FavoritedAdmin(admin.ModelAdmin):
    list_display = ("user", "filing", "created_at")