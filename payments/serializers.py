
from rest_framework import serializers
from .models import Payments
from orders.models import Order
from settings.models import PaymentModes

class OrderPKField(serializers.PrimaryKeyRelatedField):
	'''This is used to prevent information leakage in choices i.e. only the entries belonging to 
		the logged in user are displayed in the drop down'''
	def get_queryset(self):

		enterprise = self.context['request'].user.enterprise
		queryset = Order.objects.filter(enterprise=enterprise)
		return queryset

class PaymentModePKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
    	
        enterprise = self.context['request'].user.enterprise
        queryset = PaymentModes.objects.filter(enterprise=enterprise)
        return queryset


class PaymentSerializer(serializers.ModelSerializer):
	'''Serializes the Payments model'''
	class Meta:
		model=Payments
		fields=['id','payment_mode','enterprise','order','amount']

class PaymentCreateSerializer(serializers.ModelSerializer):
	'''Seializes Payments model'''
	order=OrderPKField(many=False)
	payment_mode=PaymentModePKField(many=False)
	class Meta:
		model=Payments
		fields=['order','payment_mode','amount']