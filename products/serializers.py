from rest_framework import serializers ;
from .models import Products , Category 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name' , 'parent', 'children'] 

    def get_children(self , obj):
        return CategorySerializer(obj.get_children(), many=True).data
        
class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only = True);
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='categories',
        many=True,
        write_only=True
    )
    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'categories', 'created_at', 'updated_at']        