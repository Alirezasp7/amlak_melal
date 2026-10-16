from django.urls import path
from . import views

app_name = "consultants"

urlpatterns = [
    path("", views.home, name="home"),
    path("request/<int:ct_id>/<int:pk>", views.request_detail , name="request_detail"),
    path("request/<int:ct_id>/<int:pk>/take", views.take_request , name="take_request"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("filing/<int:pk>/edit", views.filing_edit, name="filing_edit"),
    path("request/<int:ct_id>/<int:pk>/delete", views.delete_request, name="delete_request"),
    path("filing/<int:pk>/delete", views.delete_filing, name="delete_filing"),
    path("filing/<int:pk>/publish", views.publish_filing, name="publish_filing"),
    path("filing/<int:pk>/unpublish", views.unpublish_filing, name="unpublish_filing")  
]