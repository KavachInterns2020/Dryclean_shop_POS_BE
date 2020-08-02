from rest_framework import serializers
from .models import Enterprise


class EnterpriseSerializer(serializers.ModelSerializer):
	class Meta:
		model=Enterprise
		fields=['contact_name','shop_name','shop_address','phone','gst_number']


class EditProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model=Enterprise
		fields=['contact_name','shop_name','shop_address','phone']
