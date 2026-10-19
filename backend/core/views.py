from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from consultants.models import Filing
from .serializers import PublicFilingSerializer


# Create your views here.

def home(request):
    files = Filing.objects.filter(is_published=True).select_related("district")

    return render(request, "home.html", {"files":files})


def file_detail(request, pk):
    file = get_object_or_404(Filing, pk=pk, is_published=True)

    return render(request, "file_detail.html", {"file":file})


class PublicFilingViewSet(viewsets.ModelViewSet):
    queryset = Filing.objects.filter(is_published=True).select_related("district", "user")
    serializer_class = PublicFilingSerializer
    permission_classes = [AllowAny]  
