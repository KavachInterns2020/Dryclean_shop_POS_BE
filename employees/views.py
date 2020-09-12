from django.shortcuts import render
from employees.models import Employee,Role
from employees.serializers import EmployeeSerializer,EmployeeCreateSerializer,RoleSerializer,RoleCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.
class EmployeeView(LoginRequiredMixin,APIView):

	def get(self, request, format=None):
		employee = self.request.user.enterprise.employee.all()
		serializer = EmployeeSerializer(employee, many=True)
		return Response(serializer.data)


class EmployeeDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		employees=self.request.user.enterprise.employee.filter(id=pk)
		serializer = EmployeeSerializer(employees,many=True)
		return Response(serializer.data)



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


class EditEmployeeView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	def get_queryset(self):
		return self.user.enterprise.employee.all()
	serializer_class = EmployeeCreateSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

class RoleView(LoginRequiredMixin,APIView):
	def get(self, request, format=None):
		role = self.request.user.enterprise.role.all()
		serializer = RoleSerializer(role, many=True)
		return Response(serializer.data)


class RoleDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		roles=self.request.user.enterprise.role.filter(id=pk)
		serializer =RoleSerializer(roles,many=True)
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
	
class RoleEditView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	def get_queryset(self):
		return self.user.enterprise.role.all()
	serializer_class = RoleCreateSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
