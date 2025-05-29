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
            self.assertEqual(response.status_code , 200)
            self.assertEqusl(len(response.data), 1)
            self.assertEqual(response.data[0]['name'], self.product.name)
            self.assertEqual(response.data[0]['category'], self.category.id)

             



