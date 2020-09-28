from rest_framework import serializers
from .models import ProductType,ServiceType,Priority,Status,PaymentModes

class ProductTypeSerializer(serializers.ModelSerializer):
	'''Serializes ProductType model for GET requests'''
	class Meta:
		model=ProductType
		fields=['id','product_type_name','price']

class ServiceTypeSerializer(serializers.ModelSerializer):
	'''Serializes ServiceType model for GET requests'''
	class Meta:
		model=ServiceType
		fields=['id','service_type_name','price']

class PrioritySerializer(serializers.ModelSerializer):
	'''Serializes Priority model for GET requests'''
	class Meta:
		model=Priority
		fields=['id','priority_name','price']

class StatusSerializer(serializers.ModelSerializer):
	'''Serializes Status model for GET requests'''
	class Meta:
		model=Status
		fields='__all__'

class StatusCreateSerializer(serializers.ModelSerializer):
	'''Serializes Status model for POST,PUT,DELETE requests'''
	class Meta:
		model=Status
		fields=['status_name']

class PaymentModeSerializer(serializers.ModelSerializer):
	'''Serializes PaymentModes model for GET requests'''
	class Meta:
		model=PaymentModes
		fields=['id','enterprise','payment_mode_name']

class PaymentModeCreateSerializer(serializers.ModelSerializer):
	'''Serializes PaymentModes model for POST,PUT,DELETE requests'''
	class Meta:
		model=PaymentModes
		fields=['payment_mode_name']