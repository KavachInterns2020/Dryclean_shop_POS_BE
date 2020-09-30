from rest_framework import serializers
from .models import Order,OrderItem,StatusHistory
from workshops.models import Workshop
from settings.models import ProductType,ServiceType,Priority,Status
from customers.models import Customer
class ProductPKField(serializers.PrimaryKeyRelatedField):
	'''This is used to prevent information leakage in choices i.e. only the entries belonging to 
	the logged in user are displayed in the drop down'''
	def get_queryset(self):

		enterprise = self.context['request'].user.enterprise
		queryset = ProductType.objects.filter(enterprise=enterprise)
		return queryset

class ServicePKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
    	
        enterprise = self.context['request'].user.enterprise
        queryset = ServiceType.objects.filter(enterprise=enterprise)
        return queryset


class PriorityPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
    	
        enterprise = self.context['request'].user.enterprise
        queryset = Priority.objects.filter(enterprise=enterprise)
        return queryset

class StatusPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
    	
        enterprise = self.context['request'].user.enterprise
        queryset = Status.objects.filter(enterprise=enterprise)
        return queryset

class WorkshopPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
    	
        enterprise = self.context['request'].user.enterprise
        queryset = Workshop.objects.filter(enterprise=enterprise)
        return queryset

class CustomerPKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
    	
        enterprise = self.context['request'].user.enterprise
        queryset = Customer.objects.filter(enterprise=enterprise)
        return queryset

class OrderSerializer(serializers.ModelSerializer):
	'''Serializes Order model for GET requests'''
	class Meta:
		model=Order
		fields=['id','enterprise','customer','total_amount','advance_amount','pending_amount']



class OrderCreateSerializer(serializers.ModelSerializer):
	''''Seializes Order model for POST,PUT and DELETE requests'''
	customer=CustomerPKField(many=False)
	class Meta:
		model=Order
		fields=['customer','advance_amount']

class OrderItemCreateSerializer(serializers.ModelSerializer):
	'''Serializes OrderItem model for POST requests'''
	product_type=ProductPKField(many=False)
	service_type=ServicePKField(many=False)
	priority=PriorityPKField(many=False)
	class Meta:
		model=OrderItem
		fields=['id','quantity','total_amount','collection_date','expected_delivery_date',
		'actual_delivery_date','pickup_date','product_type','service_type','priority']
	
	

class OrderItemSerializer(serializers.ModelSerializer):
	'''Serializes OrderItem model for GET requests'''


	class Meta:
		model=OrderItem
		fields=['id','order','quantity','total_amount','collection_date','expected_delivery_date',
		'actual_delivery_date','pickup_date','enterprise','product_type','service_type','priority']

class OrderItemEditSerializer(serializers.ModelSerializer):
	'''Serializes OrderItem model for PUT,DELTE requests'''
	product_type=ProductPKField(many=False)
	service_type=ServicePKField(many=False)
	priority=PriorityPKField(many=False)
	class Meta:
		model=OrderItem
		fields=['quantity','collection_date','expected_delivery_date','actual_delivery_date',
		'pickup_date','product_type','service_type','priority']



class StatusHistorySerializer(serializers.ModelSerializer):
	'''Serializes StatusHistoryModel for GET requests'''
	class Meta:
		model=StatusHistory
		fields='__all__'  #all the model fields 


class StatusHistoryUpdateSerializer(serializers.ModelSerializer):
	'''Serializes StatusHistory model for POST requests'''

	status=StatusPKField(many=False)
	workshop=WorkshopPKField(many=False)
	class Meta:
		model=StatusHistory
		fields=['status','workshop','quantity','date_of_update']