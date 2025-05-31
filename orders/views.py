from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import OAuth2Authentication 
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework.response import Response
from rest_framework import status
from africastalking.SMS import SMSService
from .models import Order ,OrderItem
from .serializers import OrderSerializer,OrderItemSerializer  


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasReadWriteScope]
    required_scopes = ['read']

    def create(self , request ,*args , **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception = True)
        order = serializer.save(customer = request.user)
        order.calculate_total_amount()
        self.send_order_confirmation(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def send_order_confirmation(self, order):
        
        subject = "Order Confirmation"
        message = (
            f"Dear {order.customer.get_full_name()},\n\n"
            f"Your order #{order.id} has been received. Total amount: {order.total_amount}."
        )
        recipient_list = [order.customer.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)

        #  Africa's Talking
        admin_phone = settings.ADMIN_PHONE_NUMBER 
        sms_message = f"New order #{order.id} placed by {order.customer.username}. Total: {order.total_amount}."
        sms = SMSService(username=settings.AT_USERNAME, api_key=settings.AT_API_KEY)
        sms.send(sms_message, [admin_phone])



