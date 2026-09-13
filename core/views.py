from django.shortcuts import render

# Create your views here.z

def home(request):
    return render(request, "home.html")
