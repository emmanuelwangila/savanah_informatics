from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Order, OrderItem
from customers.models import Customer


class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='testuser1',
            password='testuserpassword123',
            email='testuser1@example.com'
        )

        self.order = Order.objects.create(
            customer=self.customer,
            total_amount=100.00  # Use the correct field name from your model
        )

        self.order_item = OrderItem.objects.create(
            order=self.order,  # Fixed typo
            product='Test product',
            quantity=3,
            price=33.78
        )

    def test_order_created(self):
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(self.order.customer.username, 'testuser1')
        self.assertEqual(self.order_item.product_name, 'Test product')