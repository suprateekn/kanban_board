from django.shortcuts import render


def home_page(request):
    return render(request, "home.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")