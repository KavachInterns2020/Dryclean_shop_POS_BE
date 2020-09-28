from rest_framework import serializers
from .models import Customer
#serialize the model fields
class CustomerSerializer(serializers.ModelSerializer):
	'''This serializer is used in GET requests to the API'''
	class Meta:
		model=Customer
		fields='__all__' #serializes all the model fields

class CustomerCreateSerializer(serializers.ModelSerializer):
	'''This serializer is used in POST, PUT and DELETE requests to the API'''
	class Meta:
		model=Customer
		fields=['customer_name','customer_email','customer_phone','customer_address']



		