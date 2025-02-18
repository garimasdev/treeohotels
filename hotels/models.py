from django.db import models
from users.models import User

class Hotel(models.Model):
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hotels")
    name = models.CharField(max_length=255)
    address = models.TextField()
    # city = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")
    room_type = models.CharField(max_length=100)  # Example: Deluxe, Suite, Standard
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_rooms = models.PositiveIntegerField()
    available_rooms = models.PositiveIntegerField()
    amenities = models.TextField(blank=True, null=True)  # List of room amenities
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.room_type} - {self.hotel.name}"



class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="room_images/")
    created_at = models.DateTimeField(auto_now_add=True)

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


