from django.contrib import admin

from bookings.models import *

admin.site.register(HotelBooking)
admin.site.register(HotelBookingCancellation)
admin.site.register(TourBooking)
admin.site.register(TourBookingCancellation)

