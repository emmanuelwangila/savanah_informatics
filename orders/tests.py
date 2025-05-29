from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Order, OrderItem
from django.contrib.auth.models import get_user_model 

Customer = get_user_model()



# Create your tests here.
class OrderAPITestCase(APITestCase):
