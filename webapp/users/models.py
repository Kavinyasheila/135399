from django.db import models
from django.contrib.auth.models import AbstractUser, Group,Permission
from django.db import models
#from .managers import CustomUserManager

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_users'  # Custom related name for groups
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_users'  # Custom related name for user_permissions
    )
    
 
    username = models.CharField(
        max_length=150,
        unique=True,
    )

    email = models.EmailField()
    #otp = models.CharField(max_length=6, null=True, blank=True)
    password = models.CharField(max_length=128)  

    def _str_(self):
        return self.username
    
    class Meta:
        db_table = 'user'
    

    
class PricePredictionInput(models.Model):
    Name = models.CharField(max_length=255)
    Quantity = models.CharField(max_length=255)  # Change from FloatField to CharField
    PredictedPrice = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.Quantity} of {self.Name}"

