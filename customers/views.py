from django.shortcuts import render
from django.shortcuts import render
from customers.models import Customer
from enterprise.models import Enterprise
from customers.serializers import CustomerSerializer,CustomerCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
class CustomerView(LoginRequiredMixin,APIView):
	'''This view allows GET requests . Details of all the customers of the current user(drycleaner)
		is displayed'''
	def get(self, request, format=None):
		customer = self.request.user.enterprise.customer.all() #selects all customers of user who is currently logged in in the browser
		serializer = CustomerSerializer(customer, many=True)
		return Response(serializer.data)

class CustomerDetailView(LoginRequiredMixin,APIView):
	'''This view allows GET requests. Details of each customer of the current user is displayed 
		in detail'''
	def get(self, request,pk,format=None):
		queryset=self.request.user.enterprise.customer.filter(id=pk) #selects customer of the logged in user with id equal to the id passed in url
		serializer = CustomerSerializer(queryset,many=True)
		return Response(serializer.data)



class CustomerCreateView(LoginRequiredMixin,generics.CreateAPIView):
	'''This view allows POST requests. New customer can be created'''
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return CustomerCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		
		'''Creates a new row in the customer table in the database'''
		if serializer.is_valid():
			
			obj=serializer.save(enterprise=self.request.user.enterprise) #set the foreign key field (enterprise) in customer model to the enterprise id of the current user
			#send an email to the email id provided in the POST request i.e. to the new customer, with the URL to his/her interface where the customer can track all of their orders
			subject=f"Welcome to {self.request.user.enterprise.shop_name}" #subject of the email
			message=f"Dear {obj.customer_name}\n Thank you for choosing our services.\n You can track your orders by clicking on the link\n" #message or body of the email
			message+= '<a href="https://google.com/">' #tracking URL. Replace it by the URL for the customer
			from_email=settings.EMAIL_HOST_USER #email id of the organization. This is set in settings.py in drycleanshop app
			to_list=[obj.customer_email] #mail ids od receipients
			send_mail(subject,message,from_email,to_list,fail_silently=False) #set fail_silently=TRUE when in production

			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditCustomerView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	'''This API view allows EDIT and DELETE requests'''
	def get_queryset(self,):
		return self.request.user.enterprise.customer.all() #selects the customer to be edited or deleted
	serializer_class = CustomerCreateSerializer
	#Method to edit the customer details
	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)
	#Method to delete the customer
	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)



	
	
