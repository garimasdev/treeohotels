from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'signup.html')


def login_view(request):
    return render(request, 'login.html')