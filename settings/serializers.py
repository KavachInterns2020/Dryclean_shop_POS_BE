from rest_framework import serializers
from .models import ProductType,ServiceType,Priority,Rate

class ProductTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=ProductType
		fields=['id','product_type_name']

class ServiceTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=ServiceType
		fields='__all__'

class PrioritySerializer(serializers.ModelSerializer):
	class Meta:
		model=Priority
		fields='__all__'

class RateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Rate
		fields='__all__'