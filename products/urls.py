from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet , CategoryAveragePriceAPIView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/<int:id>/average-price/', 
         CategoryAveragePriceAPIView.as_view(), 
         name='category-average-price'),
]