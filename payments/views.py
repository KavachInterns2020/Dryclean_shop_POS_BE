from django.shortcuts import render
from payments.models import Payments
from payments.serializers import PaymentSerializer,PaymentCreateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin,ListModelMixin
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.
class PaymentView(LoginRequiredMixin,APIView):
	'''GET, displays all the payment records'''
	def get(self, request, format=None):
		payments = self.request.user.enterprise.payment.all()
		serializer = PaymentSerializer(payments, many=True)
		return Response(serializer.data)

class PaymentDetailView(LoginRequiredMixin,APIView):
	'''GET,Displays individual payment record'''
	def get(self, request,pk,format=None):
		payments=self.request.user.enterprise.payment.filter(id=pk)
		serializer = PaymentSerializer(payments,many=True)
		return Response(serializer.data)


class PaymentCreateView(LoginRequiredMixin,generics.CreateAPIView):
	'''POST, Creates new payment records'''
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
	'''PUT,DELETE, edit or delete payment records'''
	def get_queryset(self):
		queryset=self.request.user.enterprise.payment.all()
		return queryset
	serializer_class = PaymentCreateSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)