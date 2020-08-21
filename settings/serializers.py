from rest_framework import serializers
from .models import ProductType,ServiceType,Priority

class ProductTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=ProductType
		fields=['id','product_type_name','price']

class ServiceTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model=ServiceType
		fields='__all__'

class PrioritySerializer(serializers.ModelSerializer):
	class Meta:
		model=Priority
		fields='__all__'

