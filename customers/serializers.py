from rest_framework import serializers
from .models import Customer
from django.conf import settings
from django.core.mail import send_mail
class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields='__all__'

class CustomerCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields=['customer_name','customer_email','customer_phone','customer_address']



		