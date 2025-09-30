from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .forms import CustomUserCreationForm


# Sign up view
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log in automatically after signup
            return redirect("dashboard")
    else:
        form = CustomUserCreationForm()
    return render(request, "patients/signup.html", {"form": form})


# Dashboard (protected)
@login_required
def dashboard(request):
    return render(request, "patients/dashboard.html", {"user": request.user})


# Login & Logout (using Django built-in views)
class CustomLoginView(LoginView):
    template_name = "patients/login.html"


class CustomLogoutView(LogoutView):
    template_name = "patients/logout.html"


