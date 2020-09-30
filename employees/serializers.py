from rest_framework import serializers
from .models import Employee,Role

class RolePKField(serializers.PrimaryKeyRelatedField):
	'''This is used to prevent information leakage in choices i.e. only the entries belonging to 
		the logged in user are displayed in the drop down'''
	def get_queryset(self):

		enterprise = self.context['request'].user.enterprise
		queryset = Role.objects.filter(enterprise=enterprise)
		return queryset


class EmployeeSerializer(serializers.ModelSerializer):
	'''Serializer for GET request for employees '''
	class Meta:
		model=Employee
		fields='__all__'

class EmployeeCreateSerializer(serializers.ModelSerializer):
	'''Serializer for POST,PUT,DELETE requests for employees'''
	role=RolePKField(many=False)

	class Meta:
		model=Employee
		fields=['employee_name','employee_email','employee_phone','employee_address','role']


class RoleCreateSerializer(serializers.ModelSerializer):
	'''Serializer for POST,PUT,DELETE requests for employee roles'''
	class Meta:
		model=Role
		fields=['role_name']

class RoleSerializer(serializers.ModelSerializer):
	'''Serializer for GET requests for employee roles'''
	class Meta:
		model=Role
		fields='__all__'