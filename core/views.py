from django.shortcuts import render, get_object_or_404

from consultants.models import Filing

# Create your views here.

def home(request):
    files = Filing.objects.filter(is_published=True).select_related("district")

    return render(request, "home.html", {"files":files})


def file_detail(request, pk):
    file = get_object_or_404(Filing, pk=pk, is_published=True)

    return render(request, "file_detail.html", {"file":file})
