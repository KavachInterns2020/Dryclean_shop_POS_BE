from django.db import models
from users.managers import CustomUserManager
from enterprise.models import Enterprise
from phone_field import PhoneField

# Create your models here.
class Role(models.Model):

	class Meta:

		verbose_name_plural='Roles'

		
	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='role',blank=True,null=True)
	role_name=models.CharField(max_length=100)
	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise} {self.role_name}"

class Employee(models.Model):

	class Meta:
		verbose_name_plural = "Employees"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='employee',blank=True,null=True)
	role=models.ForeignKey(Role,on_delete=models.CASCADE,related_name='employee',blank=True,null=True)
	employee_name=models.CharField(max_length=100)
	employee_email=models.EmailField(null=True,blank=True,unique=True)
	employee_phone=PhoneField(blank=True, help_text='Contact phone number',E164_only=False,unique=True)
	employee_address=models.CharField(max_length=200)

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise} - {self.employee_name} {self.employee_phone}"
