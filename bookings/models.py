from django.db import models
from users.models import User
from hotels.models import Room
from tours.models import TourPackage



class HotelBooking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hotel_bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} - {self.customer.username}"

    def calculate_total_price(self):
        """Calculate the total price based on room rate, check-in, check-out, and extra charges."""
        # Example pricing logic (you can replace this with your actual pricing logic)
        room_rate = self.room.price
        duration = (self.check_out - self.check_in).days
        self.total_price = (room_rate * duration) + self.extra_charges
        self.save()




class HotelBookingCancellation(models.Model):
    booking = models.ForeignKey(HotelBooking, on_delete=models.CASCADE, related_name="cancellations")
    cancellation_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cancellation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('processed', 'Processed')], default='pending')

    def __str__(self):
        return f"Cancellation for Booking {self.booking.id}"





class TourBooking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tour_bookings")
    tour = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name="bookings")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Discount if applicable
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} - {self.customer.username}"

    def calculate_total_price(self):
        """Calculate the final price after applying any discount."""
        pricing = self.tour.pricing
        base_price = pricing.final_price()
        self.total_price = base_price - (base_price * (self.discount / 100))
        self.save()



class TourBookingCancellation(models.Model):
    booking = models.ForeignKey(TourBooking, on_delete=models.CASCADE, related_name="cancellations")
    cancellation_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cancellation_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('processed', 'Processed')], default='pending')

    def __str__(self):
        return f"Cancellation for Tour Booking {self.booking.id}"
