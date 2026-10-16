from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("file/<int:pk>/", views.file_detail, name= "file_detail")
]
