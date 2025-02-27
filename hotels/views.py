from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'about.html')


def hotel_list(request):
    return render(request, 'hotel-grid-2.html')

