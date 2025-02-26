from django.urls import path
from .views import *


app_name = 'dashboard'


urlpatterns = [
    path('customer_dashboard/', customer_dashboard, name='db-dashboard'),
    path('vendor_dashboard/', vendor_dashboard, name='db-vendor-dashboard'),

    path('add-hotel/', add_hotel, name='add-hotel'),
    path('add-hotel-location/', add_hotel_location, name='add-hotel-location'),
    path('add-hotel-pricing/', add_hotel_pricing, name='add-hotel-pricing'),
]
