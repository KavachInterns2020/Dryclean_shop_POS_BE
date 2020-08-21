from rest_framework import serializers
from .models import Order,OrderItem

class OrderSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Order
		fields=['id','enterprise','customer','employee','total_amount','advance_amount','pending_amount']





class OrderItemSerializer(serializers.ModelSerializer):

	

	class Meta:
		model=OrderItem
		fields=['id','quantity','total_amount','collection_date','expected_delivery_date',
		'actual_delivery_date','pickup_date','order','enterprise','product_type','service_type','priority']
	
	



       