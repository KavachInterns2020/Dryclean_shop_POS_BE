from rest_framework import serializers
from .models import Employee,Role

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields='__all__'

class EmployeeCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields=['employee_name','employee_email','employee_phone','employee_address','role']

class RoleCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model=Role
		fields=['role_name']

class RoleSerializer(serializers.ModelSerializer):
	class Meta:
		model=Role
		fields='__all__'