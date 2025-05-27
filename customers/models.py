from django.db import models 
from django.contrib.auth.models import AbstractUser




# Create your models here.
class Customer(AbstractUser):
    phone_number = models.CharField(max_length=20 ,blank=True);
    address = models.TextField(blank=True);
    email_verified = models.BooleanField(default=False);
    date_of_birth = models.DateField(null = True , blank=True);
    sign_up_date = models.DateTimeField(auto_now_add=True);
    

    def __str__(self):
        return f"{self.username} ({self.email})"
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customer_set',
        related_query_name='customer',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customer_set',
        related_query_name='customer',
        blank=True,
    )
    
class Meta :
    verbose_name = "Customer"
    verbose_name_plural = "Customers"
    ordering = ['-sign_up_date']

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"    
