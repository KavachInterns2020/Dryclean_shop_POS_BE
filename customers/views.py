from django.shortcuts import render
from django.shortcuts import render
from customers.models import Customer
from customers.serializers import CustomerSerializer,CustomerCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.
class CustomerView(LoginRequiredMixin,APIView):

	def get(self, request, format=None):
		customer = Customer.objects.all()
		serializer = CustomerSerializer(customer, many=True)
		return Response(serializer.data)


class CustomerCreateView(generics.CreateAPIView):
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return CustomerCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditCustomerView(LoginRequiredMixin, APIView):
	def get_object(self, pk):
		try:
		    return Customer.objects.get(pk=pk)
		except Customer.DoesNotExist:
		    raise Http404

	def put(self, request, pk, format=None):
	    customer = self.get_object(pk)
	    serializer = CustomerSerializer(customer, data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		customer = self.get_object(pk)
		customer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


	
	
