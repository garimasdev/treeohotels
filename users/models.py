from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager



class UserRole(models.Model):
    USER_TYPES = [
        (1, 'agents'),
        (2, 'hotel_vendors'),
        (3, 'customer'),
    ]

    name = models.CharField(max_length=60)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=3)

    def __str__(self):
        return self.name + ' | User-Type: ' + str(self.user_type)
    
    class Meta:
        db_table = 'user_roles'
        verbose_name_plural = 'User Roles'


class User(AbstractUser):
    username = None
    email = models.EmailField(db_index=True, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='roles')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'



# Agents profile 
class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent_profile')
    agency_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    license_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    is_completed = models.BooleanField(default=False)  # To track if profile setup is done

    def __str__(self):
        return self.agency_name if self.agency_name else self.user.username



# Hotel vendors profile
class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    hotel_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    business_registration_number = models.CharField(max_length=100, unique=True, blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.hotel_name if self.hotel_name else self.user.username



# Customers profile
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

