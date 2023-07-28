from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import LoginForm


def login_page(request):
    forms = LoginForm(request.POST or None)
    if request.method == "POST" and forms.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated:
                return redirect("home")
        return redirect("login")

    context = {"forms": forms}
    return render(request, "accounts/login.html", context)


def logout_page(request):
    logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = firstname
        new_user.last_name = lastname
        new_user.save()
    return render(request, "accounts/signup.html")
