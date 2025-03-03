import traceback
from django.shortcuts import render
from .models import *
from django.http import JsonResponse



def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'about.html')


def hotel_list(request):
    return render(request, 'hotel-grid-2.html')


def get_hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel-grid-2.html', {'hotels': hotels})

