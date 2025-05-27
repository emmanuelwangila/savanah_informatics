from django.db import models
from mptt.models import MPTTModel , TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, 
                          null=True, blank=True, related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ['name']

class Products(models.Model):
    name = models.CharField(max_length=255 , unique = True);
    description = models.TextField(blank=True);
    price = models.DecimalField(max_digits=10, decimal_places=2);
    categories = models.ManyToManyField(Category, related_name='products');
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
