from django.shortcuts import render
from orders.models import Order,OrderItem
from orders.serializers import OrderSerializer,OrderItemSerializer,OrderItemCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
class OrderView(LoginRequiredMixin,APIView):

	def get(self, request, format=None):
		orders = Order.objects.all()
		serializer = OrderSerializer(orders, many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer=OrderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemView(LoginRequiredMixin,APIView):
	
	def get(self, request,pk,format=None):
		
		#pk = self.kwargs.get('pk')
		orderitems=OrderItem.objects.filter(order=pk)
		
		serializer = OrderItemSerializer(orderitems,many=True)
		return Response(serializer.data)



	
class OrderItemCreateView(generics.CreateAPIView):

	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return OrderItemCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		#serializer=OrderItemCreateSerializer(data=request.data)
		#pk=self.kwargs.get('pk')
		
		if serializer.is_valid():
			Order_ = get_object_or_404(Order, pk=self.kwargs.get('pk'))
			serializer.save(enterprise=self.request.user.enterprise,order=Order_)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




	

		
class EditOrderItemView(LoginRequiredMixin,APIView):

	def get_object(self,request, pk,format=None):
	    try:
	        return OrderItem.objects.get(pk=pk2)
	    except OrderItem.DoesNotExist:
	        raise Http404

	def put(self, request, format=None):
	    orderitem = self.get_object(pk)
	    serializer = OrderItemSerializer(rate, data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		orderitem = self.get_object(pk)
		orderitem.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

