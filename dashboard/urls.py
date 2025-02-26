from django.urls import path
from .views import *


app_name = 'dashboard'


urlpatterns = [
    path('customer_dashboard/', customer_dashboard, name='db-dashboard'),
    
    # Vendor dashboard
    path('vendor_dashboard/', vendor_dashboard, name='db-vendor-dashboard'),
    # ADD hotel dashboard api
    path('vendor_hotel/', vendor_hotel, name='db-vendor-add-hotel'),
    path('add-hotel/', add_hotel, name='add-hotel'),
    path('add-hotel-location/', add_hotel_location, name='add-hotel-location'),
    path('add-hotel-pricing/', add_hotel_pricing, name='add-hotel-pricing'),
    path('update-hotel-services/', update_hotel_services, name='update-hotel-services'),

    # ADD room dashboard api
    path('vendor_room/', vendor_room, name='db-vendor-add-room'),

]
