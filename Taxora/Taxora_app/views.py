from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


def index(request):
    # your existing landing page render
    return render(request, "Taxora_app/landingpg.html")

def signup(request):
    return render(request, "Taxora_app/signup.html")

# def signup_view(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             role = form.cleaned_data['role']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             # TODO: Save user in DB
#             return redirect("success_page")
#     else:
#         form = SignUpForm()
#     return render(request, "signup.html", {"form": form})

@login_required
def sme_dashboard(request):
    return render(request, "dashboard/sme_dashboard.html")
    return redirect("sme_dashboard")

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Account created successfully! Please log in.")
            return redirect("login")  # make sure 'login' is your url name
        else:
            messages.error(request, "⚠ Signup failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "auth.html", {"signup_form": form, "show_signup": True})


# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"✅ Welcome back, {username}!")
                return redirect("home")  # change "home" to your dashboard view
            else:
                messages.error(request, "❌ Invalid username or password.")
        else:
            messages.error(request, "❌ Invalid login details.")
    else:
        form = AuthenticationForm()
    return render(request, "signup.html", {"login_form": form, "show_signup": False})


# Logout View (optional)
def logout_view(request):
    logout(request)
    messages.info(request, "👋 You have been logged out successfully.")
    return redirect("login")