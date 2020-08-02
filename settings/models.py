from django.db import models
from users.managers import CustomUserManager
from enterprise.models import Enterprise
# Create your models here.



class ProductType(models.Model):
	id=models.AutoField(primary_key=True)
	product_type_name=models.CharField(max_length=100,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='product')

	objects=CustomUserManager()

class ServiceType(models.Model):
	id=models.AutoField(primary_key=True)
	
	service_type_name=models.CharField(max_length=100,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='service')
	objects=CustomUserManager()

class Priority(models.Model):
	id=models.AutoField(primary_key=True)
	
	priority_name=models.CharField(max_length=100,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='priority')
	objects=CustomUserManager()

class Rate(models.Model):
	id=models.AutoField(primary_key=True)
	price=models.DecimalField(max_digits=6,decimal_places=2,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='rate')
	product=models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='product')
	service=models.ForeignKey(ServiceType,on_delete=models.CASCADE,related_name='service')
	priority=models.ForeignKey(Priority,on_delete=models.CASCADE,related_name='priority')

	objects=CustomUserManager()
