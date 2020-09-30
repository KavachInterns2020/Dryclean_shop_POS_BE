from rest_framework import serializers
from .models import Enterprise


class EnterpriseSerializer(serializers.ModelSerializer):
	'''Serializes Enterprise model.Provides details of the Drycleaning shop'''
	class Meta:
		model=Enterprise
		fields=['contact_name','shop_name','shop_address','phone','gst_number']


class EditProfileSerializer(serializers.ModelSerializer):
	'''Serializes enterprise model.Provides details which are allowed to be edited by the user'''
	class Meta:
		model=Enterprise
		fields=['contact_name','shop_name','shop_address','phone','gst_number']

