from django.urls import reverse 
from rest_framework.test import APITestCase 
from .models import Products, Category

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Products.objects.create(
            name="Smartphone",
            description="Latest smart phone",
            price=699.99,
        )
        self.product.categories.set([self.category])

    def test_get_product_list(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.product.name)
        # Compare the id inside the category dict
        self.assertEqual(response.data[0]['categories'][0]['id'], self.category.id)

    def test_category_average_price(self):
        response = self.client.get(
            reverse('category-average-price', args=[self.category.id])
        )
        self.assertEqual(response.status_code, 200)
        # Compare as floats with precision
        self.assertAlmostEqual(float(response.data['average-price']), float(self.product.price), places=2)
        self.assertEqual(response.data['category'], self.category.id)
        self.assertEqual(response.data['category_name'], self.category.name)