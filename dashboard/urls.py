from django.urls import path
from .views import customer_dashboard, vendor_dashboard


app_name = 'dashboard'


urlpatterns = [
    path('customer_dashboard/', customer_dashboard, name='db-dashboard'),
    path('vendor_dashboard/', vendor_dashboard, name='db-vendor-dashboard'),
]
