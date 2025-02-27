from django.urls import path
from . import views

app_name = "hotels"

urlpatterns = [
    path('aboutus/', views.aboutus, name='aboutus'),
    path('homepage/', views.homepage, name='homepage'),


    path('hotel-list-2/', views.hotel_list, name='hotel-list'),

]