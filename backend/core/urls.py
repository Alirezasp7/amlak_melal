from django.urls import path, include

from rest_framework import routers

from .views import home, file_detail, PublicFilingViewSet

router = routers.DefaultRouter()
router.register(r'public-filings', PublicFilingViewSet, basename='public-filings')

app_name = "core"

urlpatterns = [
    path("", include(router.urls)),
    path("", home, name="home"),
    path("file/<int:pk>/", file_detail, name= "file_detail")
]
