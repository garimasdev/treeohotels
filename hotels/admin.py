from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Hotel)
admin.site.register(HotelReview)
admin.site.register(Room)
admin.site.register(RoomImage)
admin.site.register(RoomPricing)