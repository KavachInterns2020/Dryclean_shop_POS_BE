from rest_framework import serializers
from .models import Workshop

class WorkshopSerializer(serializers.ModelSerializer):
	class Meta:
		model=Workshop
		fields=['id','enterprise','workshop_name','workshop_phone','workshop_email','workshop_address']

class WorkshopCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Workshop
		fields=['workshop_name','workshop_phone','workshop_email','workshop_address']
