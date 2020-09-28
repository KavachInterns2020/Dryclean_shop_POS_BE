from django.shortcuts import render
from customers.models import Customer
from orders.models import Order,OrderItem,StatusHistory
from orders.serializers import OrderSerializer,OrderCreateSerializer,OrderItemSerializer,OrderItemCreateSerializer,OrderItemEditSerializer,StatusHistorySerializer,StatusHistoryUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin,ListModelMixin

# Create your views here.
class OrderView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):
	'''GET, displays all orders taken by the logged in user'''
	def get_queryset(self):
		return self.request.user.enterprise.order.all()
	#queryset=Order.objects.all()
	serializer_class = OrderSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)


class OrderDetailView(LoginRequiredMixin,APIView):
	'''GET, displays individual orders taken by the loggedin user'''
	def get(self, request,pk,format=None):
		
		queryset=self.request.user.enterprise.order.filter(id=pk)
		
		#pk = self.kwargs.get('pk')
		#orderitems=Order.objects.filter(id=pk)

		serializer = OrderSerializer(queryset,many=True)

		
		return Response(serializer.data)



class OrderCreateView(LoginRequiredMixin,generics.CreateAPIView):
	'''POST, creates new orders'''
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return OrderCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderEditView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	'''PUT,DELETE, edits or deletes orders'''
	def get_queryset(self):
		queryset=self.request.user.enterprise.order.all()
		return queryset

	serializer_class = OrderCreateSerializer

	def put(self, request, *args, **kwargs):
		
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		
		return self.destroy(request, *args, **kwargs)

class OrderItemView(LoginRequiredMixin,APIView):
	'''GET, displays all the order items of a particular order'''
	def get(self, request,pk,format=None):
		
		#pk = self.kwargs.get('pk')
		#orders=self.request.user.enterprise.order.filter(id=pk)
		orderitems=self.request.user.enterprise.orderitem.filter(order=pk)

		serializer = OrderItemSerializer(orderitems,many=True)

		
		return Response(serializer.data)

class OrderItemDetailView(LoginRequiredMixin,APIView):
	'''GET, displays individual order items of a particular order'''
	def get(self, request,pk,pk_alt,format=None):
		
		#pk = self.kwargs.get('pk')
		orderitems=self.request.user.enterprise.orderitem.filter(order=pk,id=pk_alt)
		serializer = OrderItemSerializer(orderitems,many=True)
		return Response(serializer.data)



	
class OrderItemCreateView(LoginRequiredMixin,generics.CreateAPIView):
	'''POST,creates new order items within a particular order'''
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return OrderItemCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		#serializer=OrderItemCreateSerializer(data=request.data)
		#pk=self.kwargs.get('pk')
		
		if serializer.is_valid():
			Order_ = get_object_or_404(Order, pk=self.kwargs.get('pk')) #order field is automatically filled with the pk value in the URL
			serializer.save(enterprise=self.request.user.enterprise,order=Order_)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




	

		
class EditOrderItemView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	'''PUT,DELETE, edits or deletes order items'''
	def get_queryset(self):
		queryset=self.request.user.enterprise.orderitem.all()
		return queryset
	serializer_class = OrderItemEditSerializer

	def put(self, request, *args, **kwargs):
		
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		
		return self.destroy(request, *args, **kwargs)	



class StatusHistoryView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):
	'''GET, displays status history'''
	def get_queryset(self):
		return self.request.user.enterprise.statushistory.all()
	serializer_class = StatusHistorySerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

	

class StatusHistoryUpdateView(LoginRequiredMixin,generics.CreateAPIView):
	'''POST, creates a new update for the status history'''
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return StatusHistoryUpdateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		
		
		if serializer.is_valid():
			Orderitem_ = get_object_or_404(OrderItem, pk=self.kwargs.get('pk_alt')) #order item field is automatically filled using pk_alt in the URL
			order_=get_object_or_404(Order,pk=self.kwargs.get('pk'))
			#customer_=get_object_or_404(Customer,pk=order_.customer.id)
			
			serializer.save(enterprise=self.request.user.enterprise,order_item=Orderitem_,order=order_)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








