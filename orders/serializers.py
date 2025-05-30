from rest_framework import serializers
from products.serializers import ProductSerializer 
from.models import Order , OrderItem



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only = True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset = ProductSerializer().Meta.model.objects.all(),
        source = 'product',
        write_only = True
    )

    class Meta:
        model = OrderItem
        fields = ['id' , 'product', 'product_id', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    customer = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'status', 'total_amount',
            'items', 'created_at', 'updated_at'
        ]
        read_only_fields = ['total_amount', 'created_at', 'updated_at']


    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total_amount = 0


        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = item_data['price']
            total_amount += quantity * price

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price
        )
        order.total_amount = total_amount
        order.save()
        return order
        
        
        
        
        
        
        
        
        
        
        
        




