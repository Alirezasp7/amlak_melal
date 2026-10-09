from django.urls import path
from . import views

app_name = "consultants"

urlpatterns = [
    path("", views.home, name="home"),
    path("request/<int:ct_id>/<int:pk>", views.request_detail , name="request_detail")   
]