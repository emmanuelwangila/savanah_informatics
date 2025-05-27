from django.db import models
from customers.models import Customer 
from products.models  import Products

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders');
    created_at = models.DateTimeField(auto_now_add=True);
    updated_at = models.DateTimeField(auto_now=True);
    total_amount = models.DecimalField(max_digits=10, decimal_places=2);
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ] ;
    status = models.CharField(max_length=10,choices=STATUS_CHOICES , default='PENDING');
    

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"

    def calculate_total_amount(self):
        total = sum(item.get_cost() for item in self.items.all())
        self.total_amount = total
        self.save()
        return total
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items');
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='order_items');
    quantity = models.PositiveIntegerField(default=1);
    price = models.DecimalField(max_digits=10, decimal_places=2);


    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}";

    def get_cost(self):
       return self.quantity * self.price  