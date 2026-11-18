from django.contrib import admin

from .models import Favorites
# Register your models here.

@admin.register(Favorites)
class FavoritedAdmin(admin.ModelAdmin):
    list_display = ("user", "filing", "created_at")