from django.shortcuts import render
from settings.models import ProductType,ServiceType,Priority,Status
from settings.serializers import ProductTypeSerializer,ServiceTypeSerializer,PrioritySerializer,StatusSerializer,StatusCreateSerializer
from django.http import Http404
import rest_framework.mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,ListModelMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.
class ProductTypeView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):

	queryset = ProductType.objects.all()
	serializer_class = ProductTypeSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)



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

class DeleteProductType(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	queryset = ProductType.objects.all()
	serializer_class = ProductTypeSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)	



class ServiceTypeView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):
	
	queryset = ServiceType.objects.all()
	serializer_class = ServiceTypeSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

	

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

class DeleteServiceType(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	queryset = ServiceType.objects.all()
	serializer_class = ServiceTypeSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
	
	


class PriorityView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):

	queryset = Priority.objects.all()
	serializer_class = PrioritySerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)


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

class DeletePriority(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	queryset = Priority.objects.all()
	serializer_class = PrioritySerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
	

class StatusView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):
	queryset = Status.objects.all()
	serializer_class = StatusSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)



class StatusCreateView(generics.CreateAPIView):

	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return StatusCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
	
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusEditView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):

	queryset = Status.objects.all()
	serializer_class = StatusCreateSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)



	
			
	    