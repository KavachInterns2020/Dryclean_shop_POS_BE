from rest_framework import serializers
from .models import Order,OrderItem

class OrderSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Order
		fields=['id','enterprise','customer','employee','total_amount','advance_amount','pending_amount']





class OrderItemCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model=OrderItem
		fields=['id','quantity','total_amount','collection_date','expected_delivery_date',
		'actual_delivery_date','pickup_date','product_type','service_type','priority']
	
	

class OrderItemSerializer(serializers.ModelSerializer):
	class Meta:
		model=OrderItem
		fields=['id','order','quantity','total_amount','collection_date','expected_delivery_date',
		'actual_delivery_date','pickup_date','enterprise','product_type','service_type','priority']


       