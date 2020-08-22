from django.shortcuts import render
from settings.models import ProductType,ServiceType,Priority
from settings.serializers import ProductTypeSerializer,ServiceTypeSerializer,PrioritySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.
class ProductTypeView(LoginRequiredMixin,APIView):

	def get(self, request, format=None):
		products = ProductType.objects.all()
		serializer = ProductTypeSerializer(products, many=True)
		return Response(serializer.data)


class ProductTypeCreateView(generics.CreateAPIView):
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return ProductTypeSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
	
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteProductType(LoginRequiredMixin,APIView):
	def get_object(self, pk):
	    try:
	        return ProductType.objects.get(pk=pk)
	    except ProductType.DoesNotExist:
	        raise Http404

	
	def delete(self, request, pk, format=None):
		product = self.get_object(pk)
		product.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class ServiceTypeView(LoginRequiredMixin,APIView):
	
	def get(self, request, format=None):
		services = ServiceType.objects.all()
		serializer = ServiceTypeSerializer(services, many=True)
		return Response(serializer.data)

	

class ServiceTypeCreateView(generics.CreateAPIView):
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return ServiceTypeSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
	
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteServiceType(LoginRequiredMixin,APIView):

	def get_object(self,pk):
		try:
			return ServiceType.objects.get(pk=pk)
		except ServiceType.DoesNotExist:
			raise Http404

	def delete(self, request, pk, format=None):
		service = self.get_object(pk)
		service.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class PriorityView(LoginRequiredMixin,APIView):
	

	def get(self,request,format=None):
		priorities=Priority.objects.all()
		serializer=PrioritySerializer(priorities, many=True)
		return Response(serializer.data)


class PriorityCreateView(generics.CreateAPIView):
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return PrioritySerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
	
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletePriority(LoginRequiredMixin,APIView):

	def get_object(self,pk):
		try:
			return Priority.objects.get(pk=pk)
		except ServiceType.DoesNotExist:
			raise Http404

	def delete(self, request, pk, format=None):
		priority = self.get_object(pk)
		priority.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

