from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(HotelServices)
admin.site.register(HotelPolicy)
admin.site.register(Amenity)
admin.site.register(AmenityCategory)
admin.site.register(HotelReview)
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(RoomPricing)
