from rest_framework.test import APITestCase
from .models import Order, OrderItem
from customers.models import Customer  # Use your custom user model
from products.models import Products

class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='testuser1',
            password='testuserpassword123',
            email='testuser1@example.com'
        )
        self.product = Products.objects.create(
            name='Test Product',
            description='A product for testing',
            price=33.78
        )
        self.order = Order.objects.create(
            customer=self.customer,
            total_amount=100.00
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3,
            price=33.78
        )

    def test_order_created(self):
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(OrderItem.objects.count(), 1)
        self.assertEqual(self.order.customer.username, 'testuser1')
        self.assertEqual(self.order_item.product.name, 'Test Product')