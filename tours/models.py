from django.db import models
from users.models import User  

class TourPackage(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tour_packages")
    title = models.CharField(max_length=255)
    description = models.TextField()
    destination = models.CharField(max_length=255)  # City/Country
    duration = models.PositiveIntegerField()  # In days
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class TourImage(models.Model):
    tour = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="tour_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.tour.title}"




class TourPricing(models.Model):
    tour = models.OneToOneField(TourPackage, on_delete=models.CASCADE, related_name="pricing")
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    gst_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)  # Default 5% GST
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Optional extra charges

    def final_price(self):
        """Calculate final price after discount and GST."""
        price_after_discount = self.base_price - (self.base_price * (self.discount_percentage / 100))
        total_price = price_after_discount + (price_after_discount * (self.gst_percentage / 100)) + self.extra_charges
        return round(total_price, 2)

    def __str__(self):
        return f"Pricing for {self.tour.title}"



class Itinerary(models.Model):
    tour = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name="itineraries")
    day_number = models.PositiveIntegerField()
    details = models.TextField()

    def __str__(self):
        return f"Day {self.day_number} - {self.tour.title}"

    class Meta:
        unique_together = ('tour', 'day_number')




class TourInclusionsExclusions(models.Model):
    tour = models.OneToOneField(TourPackage, on_delete=models.CASCADE, related_name="inclusions_exclusions")
    inclusions = models.TextField(help_text="Things included in the package")
    exclusions = models.TextField(help_text="Things not included in the package")

    def __str__(self):
        return f"Inclusions/Exclusions for {self.tour.title}"





class TourPolicy(models.Model):
    tour = models.OneToOneField(TourPackage, on_delete=models.CASCADE, related_name="policies")
    cancellation_policy = models.TextField()
    refund_policy = models.TextField()
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Policies for {self.tour.title}"






class TourPackageReview(models.Model):
    tour = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name="reviews")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tour_reviews")
    rating = models.PositiveIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    review_text = models.TextField()

    def __str__(self):
        return f"Review by {self.customer.username} for {self.tour.title}"
