from rest_framework import serializers
from .models import Order,OrderItem,StatusHistory

class OrderSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Order
		fields=['id','enterprise','customer','employee','total_amount','advance_amount','pending_amount']



class OrderCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Order
		fields=['customer','employee','advance_amount']






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

class OrderItemEditSerializer(serializers.ModelSerializer):
	class Meta:
		model=OrderItem
		fields=['quantity','collection_date','expected_delivery_date','actual_delivery_date',
		'pickup_date','product_type','service_type','priority']



class StatusHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model=StatusHistory
		fields='__all__'

class StatusHistoryUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model=StatusHistory
		fields=['status','quantity','date_of_update']