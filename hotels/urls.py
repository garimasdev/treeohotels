from django.urls import path
from . import views

app_name = "hotels"

urlpatterns = [
    path('aboutus/', views.aboutus, name='aboutus'),
    path('hotel-list-2/', views.hotel_list, name='hotel-list'),

    path('get_hotel_list/', views.get_hotel_list, name='get-hotel-list'),


]