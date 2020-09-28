from rest_framework import serializers
from .models import Order,OrderItem,StatusHistory

class OrderSerializer(serializers.ModelSerializer):
	'''Serializes Order model for GET requests'''
	class Meta:
		model=Order
		fields=['id','enterprise','customer','total_amount','advance_amount','pending_amount']



class OrderCreateSerializer(serializers.ModelSerializer):
	''''Seializes Order model for POST,PUT and DELETE requests'''
	class Meta:
		model=Order
		fields=['customer','advance_amount']

class OrderItemCreateSerializer(serializers.ModelSerializer):
	'''Serializes OrderItem model for POST requests'''
	class Meta:
		model=OrderItem
		fields=['id','quantity','total_amount','collection_date','expected_delivery_date',
		'actual_delivery_date','pickup_date','product_type','service_type','priority']
	
	

class OrderItemSerializer(serializers.ModelSerializer):
	'''Serializes OrderItem model for GET requests'''
	class Meta:
		model=OrderItem
		fields=['id','order','quantity','total_amount','collection_date','expected_delivery_date',
		'actual_delivery_date','pickup_date','enterprise','product_type','service_type','priority']

class OrderItemEditSerializer(serializers.ModelSerializer):
	'''Serializes OrderItem model for PUT,DELTE requests'''
	class Meta:
		model=OrderItem
		fields=['quantity','collection_date','expected_delivery_date','actual_delivery_date',
		'pickup_date','product_type','service_type','priority']



class StatusHistorySerializer(serializers.ModelSerializer):
	'''Serializes StatusHistoryModel for GET requests'''
	class Meta:
		model=StatusHistory
		fields='__all__'  #all the model fields 


class StatusHistoryUpdateSerializer(serializers.ModelSerializer):
	'''Serializes StatusHistory model for POST requests'''
	class Meta:
		model=StatusHistory
		fields=['status','quantity','date_of_update']