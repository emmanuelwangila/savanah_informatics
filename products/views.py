from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.db.models import Avg
from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id', None)

        if category_id:
            category = Category.objects.get(id=category_id)
            descendants = category.get_descendants(include_self=True)
            queryset = queryset.filter(categories__in=descendants)

        return queryset.distinct()

class CategoryAveragePriceAPIView(generics.GenericAPIView):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        descendants = category.get_descendants(include_self=True)

        # Remove is_active if not present in Products model
        avg_price = Products.objects.filter(
            categories__in=descendants
        ).aggregate(avg_price=Avg('price'))['avg_price'] or 0

        return Response({
            'category': category.id,
            'category_name': category.name,
            'average-price': avg_price
        })