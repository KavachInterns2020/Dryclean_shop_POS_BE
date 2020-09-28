from django.db import models
from users.managers import CustomUserManager
from enterprise.models import Enterprise


# Create your models here.
class Role(models.Model):
	'''This model class creates a Role table in the database for storing employee roles'''
	class Meta:

		verbose_name_plural='Roles'

		
	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='role',blank=True,null=True)
	role_name=models.CharField(max_length=100)
	objects=CustomUserManager() #since we have used custom user and manager all the model classes are appended with this line

	def __str__(self):
		return f"{self.id} {self.enterprise} {self.role_name}"

class Employee(models.Model):
	'''This model class creates Employee table in the database to store employee details'''

	class Meta:
		verbose_name_plural = "Employees"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='employee',blank=True,null=True)
	role=models.ForeignKey(Role,on_delete=models.CASCADE,related_name='employee',blank=True,null=True)
	employee_name=models.CharField(max_length=100)
	employee_email=models.EmailField(null=True,blank=True,unique=True)
	employee_phone=models.CharField(null=True,blank=True,max_length=13)
	employee_address=models.CharField(max_length=200)

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise} - {self.employee_name} {self.employee_phone}"
