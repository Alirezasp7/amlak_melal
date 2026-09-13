from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView

from .forms import SignUpForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('/') 
    else:
        form = SignUpForm()
    return render(request, "/home/alirezasp/Documents/amlak_melal/templates/accounts/signup.html", {"form": form})



class CustomLoginView(LoginView):
    template_name = "/home/alirezasp/Documents/amlak_melal/templates/accounts/login.html"
    redirect_authenticated_user = True



def logout(request):
    logout(request)
    return redirect("/")