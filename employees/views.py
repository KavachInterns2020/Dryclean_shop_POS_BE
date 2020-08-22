from django.shortcuts import render
from employees.models import Employee,Role
from employees.serializers import EmployeeSerializer,EmployeeCreateSerializer,RoleSerializer,RoleCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.
class EmployeeView(LoginRequiredMixin,APIView):

	def get(self, request, format=None):
		employee = Employee.objects.all()
		serializer = EmployeeSerializer(employee, many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer=EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeCreateView(generics.CreateAPIView):
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return EmployeeCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditEmployeeView(LoginRequiredMixin,APIView):
	def get_object(self, pk):
	    try:
	        return Employee.objects.get(pk=pk)
	    except Employee.DoesNotExist:
	        raise Http404

	def put(self,request,pk,format=None):
		employee=self.get_object(pk)
		serializer = CustomerSerializer(employee, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		employee = self.get_object(pk)
		employee.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class RoleView(LoginRequiredMixin,APIView):
	def get(self, request, format=None):
		role = Role.objects.all()
		serializer = RoleSerializer(, many=True)
		return Response(serializer.data)

class RoleCreateView(generics.CreateAPIView):

	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return RoleCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

