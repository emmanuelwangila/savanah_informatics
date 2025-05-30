from rest_framework.test import APITestCase
from .models import Order, OrderItem
from unittest.mock import patch
from django.urls import reverse 
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



class OrderEmailTestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create_user(
            username='testuser2',
            password='testuserpassword12345',
            email='emmanuelwangila1@gmail.com'
        )
        self.product = Products.objects.create(
            name='New product',
            description='latest one',
            price=960.89
        )
        self.client.force_authenticate(user=self.customer)

    @patch('orders.views.SMSService.send')
    def test_order_sms_sent_to_admin(self, mock_sms_send):
        order_data = {
            "items": [
                {
                    "product": self.product.id,
                    "quantity": 3,
                    "price": 960.89
                }
            ]
        }
        response = self.client.post(reverse('order-list'), order_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(mock_sms_send.called)




















