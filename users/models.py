from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager



class UserRole(models.Model):
    USER_TYPES = [
        (1, 'agents'),
        (2, 'hotel_vendors'),
    ]

    name = models.CharField(max_length=60)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=2)

    def __str__(self):
        return self.name + ' | User-Type: ' + str(self.user_type)
    
    class Meta:
        db_table = 'user_roles'
        verbose_name_plural = 'User Roles'


class User(AbstractUser):
    username = None
    email = models.EmailField(db_index=True, unique=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE, related_name='roles')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'

