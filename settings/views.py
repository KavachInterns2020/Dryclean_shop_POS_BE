from django.shortcuts import render
from settings.models import ProductType,ServiceType,Priority,Status,PaymentModes
from settings.serializers import ProductTypeSerializer,ServiceTypeSerializer,PrioritySerializer,StatusSerializer,StatusCreateSerializer,PaymentModeSerializer,PaymentModeCreateSerializer
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

	def get_queryset(self):
		return self.request.user.enterprise.product.all()
	serializer_class = ProductTypeSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)


class ProductTypeDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		product=self.request.user.enterprise.product.filter(id=pk)
		serializer = ProductTypeSerializer(product,many=True)
		return Response(serializer.data)

class ProductTypeCreateView(LoginRequiredMixin,generics.CreateAPIView):
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
	def get_queryset(self):
		return self.request.user.enterprise.product.all()
	serializer_class = ProductTypeSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)	



class ServiceTypeView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):
	
	def get_queryset(self):
		return self.request.user.enterprise.service.all()
	serializer_class = ServiceTypeSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

class ServiceTypeDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		service=self.request.user.enterprise.service.filter(id=pk)
		serializer = ServiceTypeSerializer(service,many=True)
		return Response(serializer.data)	

class ServiceTypeCreateView(LoginRequiredMixin,generics.CreateAPIView):
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
	def get_queryset(self):
		return self.request.user.enterprise.service.all()
	serializer_class = ServiceTypeSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
	
	


class PriorityView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):

	def get_queryset(self):
		return self.request.user.enterprise.priority.all()
	serializer_class = PrioritySerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)


class PriorityDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		priority=self.request.user.enterprise.priority.filter(id=pk)
		serializer = PrioritySerializer(priority,many=True)
		return Response(serializer.data)

class PriorityCreateView(LoginRequiredMixin,generics.CreateAPIView):
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
	def get_queryset(self):
		return self.request.user.enterprise.priority.all()
	serializer_class = PrioritySerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
	

class StatusView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):
	def get_queryset(self):
		return self.request.user.enterprise.status.all()
	serializer_class = StatusSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

class StatusDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		status=self.request.user.enterprise.status.filter(id=pk)
		serializer = StatusSerializer(status,many=True)
		return Response(serializer.data)

class StatusCreateView(LoginRequiredMixin,generics.CreateAPIView):

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

	def get_queryset(self):
		return self.request.user.enterprise.status.all()
	serializer_class = StatusCreateSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


class PaymentModeView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):
	def get_queryset(self):
		return self.request.user.enterprise.payment_mode.all()
	serializer_class = PaymentModeSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

class PaymentModeDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		payment_mode=self.request.user.enterprise.payment_mode.filter(id=pk)
		serializer = PaymentModeSerializer(payment_mode,many=True)
		return Response(serializer.data)

class PaymentModeCreateView(LoginRequiredMixin,generics.CreateAPIView):

	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return PaymentModeCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
	
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	    
class PaymentModeEditView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	def get_queryset(self):
		return self.request.user.enterprise.payment_mode.all()
	serializer_class = PaymentModeCreateSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)