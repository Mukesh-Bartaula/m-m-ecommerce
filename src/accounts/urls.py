from django.contrib import admin
from django.urls import path
from .views import login_page, signup, logout_page

urlpatterns = [
    path("login/", login_page, name="login"),
    path("logout_page/", logout_page, name="logout_page"),
    path("signup/", signup, name="signup"),
]
