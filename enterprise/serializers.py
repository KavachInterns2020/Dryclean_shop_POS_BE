from rest_framework import serializers
from .models import Enterprise,Payments


class EnterpriseSerializer(serializers.ModelSerializer):
	class Meta:
		model=Enterprise
		fields=['contact_name','shop_name','shop_address','phone','gst_number']


class EditProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=Enterprise
		fields=['contact_name','shop_name','shop_address','phone']

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Payments
		fields=['id','payment_mode','enterprise','order','amount']

class PaymentCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Payments
		fields=['order','payment_mode','amount']