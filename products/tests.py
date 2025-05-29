from django.test import TestCase
from django.urls import reverse 
from rest_framework import APITestCase 
from .models import Products ,Category

# Create your tests here.

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product =Products.objects.create(
            name="Smartphone",
            description ="Latest smart phone",
            price = 699.99,
            category=self.category

        )
        def test_get_product_list(self):
            response = self.client.get(reverse('product-list'))
            


