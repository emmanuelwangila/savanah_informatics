from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from.models import Products, Category
from rest_framework import response
from django.db.models import Avg

from .serializers import ProductSerializer , CategorySerializer


# Create your views here.
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
            category = Category.obects.get(id=category_id);
            descendants = category.get_descendants(include_self = True);
            queryset = queryset.filter(categories__in= descendants);

        return queryset.distinct()
    

class CategoryAveragePriceAPIView(generics.GenericAPIView):
    def get(self , request ,id):
        Category.objects.get(id= id);
        descendants =Category.get_descendants(include_self=True)
        
        avg_price = Products.objects.filter(
            categories__in=descendants,
            is_active=True
        ).aggregate(avg_price=Avg('price'))['avg_price'] or 0
        
        return response({
            'category_id': id,
            'category_name': Category.name,
            'average_price': avg_price
        })    
