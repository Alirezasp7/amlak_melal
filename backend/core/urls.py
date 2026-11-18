from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PublicFilingViewSet, ToggleFavoriteView, ListFavoriteView

router = DefaultRouter()
router.register(r'public-filings', PublicFilingViewSet, basename='public-filings')

app_name = "core"

urlpatterns = [
    path('', include(router.urls)),
    path("favorites/toggle/<int:filing_id>/", ToggleFavoriteView.as_view(), name='favorite-toggle'),
    path("favorites/", ListFavoriteView.as_view(), name='favorite-list')
]
