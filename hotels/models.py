from django.db import models
from users.models import User

class Hotel(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hotels", db_index=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    description = models.TextField(blank=True, null=True)
    youtube_video = models.URLField(blank=True, null=True)
    hotel_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Images for the hotel
    banner_images = models.ManyToManyField('HotelImage', related_name='banner_images', blank=True)
    featured_images = models.ManyToManyField('HotelImage', related_name='featured_images', blank=True)
    gallery_images = models.ManyToManyField('HotelImage', related_name='hotel_gallery', blank=True)

    # Policies for the hotel
    policies = models.ManyToManyField('HotelPolicy', related_name='hotel_policies', blank=True)



    def __str__(self):
        return self.name



class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_images")
    image = models.ImageField(upload_to='hotels/images/')
    image_type = models.CharField(max_length=50, choices=[('banner', 'Banner'), ('featured', 'Featured'), ('gallery', 'Gallery')])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="images")
    # image = models.ImageField(upload_to="hotel_images/")
    # is_banner = models.BooleanField(default=False)
    # is_featured = models.BooleanField(default=False)
    # is_gallery = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.image_type}) - {self.image.name}"



class HotelPolicy(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel_policies")
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title



class HotelPricing(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="pricing_details")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    minimum_advance_reservations = models.IntegerField()
    minimum_day_stay_requirements = models.IntegerField()

    def __str__(self):
        return self.hotel.name



class HotelServices(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="services")
    apartment = models.BooleanField(default=False)
    boat = models.BooleanField(default=False)
    holiday_home = models.BooleanField(default=False)
    villa = models.BooleanField(default=False)
    cabin = models.BooleanField(default=False)
    hostel = models.BooleanField(default=False)
    lodge = models.BooleanField(default=False)
    mansion = models.BooleanField(default=False)
    banquet = models.BooleanField(default=False)

    # facilities
    swimming_pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    spa = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)
    bar = models.BooleanField(default=False)
    free_wifi = models.BooleanField(default=False)
    conference_room = models.BooleanField(default=False)

    # HotelService
    room_service = models.BooleanField(default=False)
    cleaning_service = models.BooleanField(default=False)
    laundry_service = models.BooleanField(default=False)
    shuttle_service = models.BooleanField(default=False)
    concierge_service = models.BooleanField(default=False)
    hour24_reception = models.BooleanField(default=False)






class AmenityCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Amenity(models.Model):
    category = models.ForeignKey(AmenityCategory, on_delete=models.CASCADE, related_name="amenities")
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.CharField(max_length=100)  # Example: Deluxe, Suite, Standard
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available_rooms = models.PositiveIntegerField(blank=True, null=True)
    sleeps = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    amenities = models.ManyToManyField(Amenity, blank=True)


    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"



class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="room_images/")

    def __str__(self):
        return f"Image for {self.room.room_type} - {self.room.hotel.name}"



class RoomPricing(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, related_name="pricing")
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def final_price(self):
        """Calculate final price after tax and discount."""
        price_after_discount = self.room.price_per_night - (self.room.price_per_night * (self.discount_percentage / 100))
        total_price = price_after_discount + (price_after_discount * (self.tax_percentage / 100)) + self.extra_charges
        return round(total_price, 2)

    def __str__(self):
        return f"Pricing for {self.room.room_type} - {self.room.hotel.name}"



class HotelReview(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reviews")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hotel_reviews")
    rating = models.PositiveIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.customer.username} for {self.hotel.name}"


