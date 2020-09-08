from django.shortcuts import render
from enterprise.models import Enterprise,Payments
from enterprise.serializers import EnterpriseSerializer,EditProfileSerializer,PaymentSerializer,PaymentCreateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin,ListModelMixin


# Create your views here.
class Profile(LoginRequiredMixin,APIView):

	def get_object(self, pk):
	    try:
	        return Enterprise.objects.get(pk=pk)
	    except Enterprise.DoesNotExist:
	        raise Http404

	def get(self, request, pk, format=None):
	    enterprise = self.get_object(pk)
	    serializer = EnterpriseSerializer(enterprise)
	    return Response(serializer.data)

class EditProfile(LoginRequiredMixin,APIView):
	def get_object(self,pk):
		try:
			return Enterprise.objects.get(pk=pk)
		except Enterprise.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
	    enterprise = self.get_object(pk)
	    serializer = EditProfileSerializer(enterprise, data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentView(LoginRequiredMixin,ListModelMixin,generics.GenericAPIView):
	queryset = Payments.objects.all()
	serializer_class = PaymentSerializer

	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

class PaymentDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		payments=Payments.objects.filter(id=pk)
		serializer =PaymentSerializer(payments,many=True)
		return Response(serializer.data)

class PaymentCreateView(generics.CreateAPIView):

	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return PaymentCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		
		if serializer.is_valid():
			serializer.save(enterprise=self.request.user.enterprise)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentEditView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	queryset = Payments.objects.all()
	serializer_class = PaymentCreateSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)