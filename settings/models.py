from django.db import models
from users.managers import CustomUserManager
from enterprise.models import Enterprise
# Create your models here.



class ProductType(models.Model):
	'''This mocel is for product types (eg. shirt,pant,saree etc.)'''
	class Meta:
		verbose_name_plural = "Product types"

	id=models.AutoField(primary_key=True)
	product_type_name=models.CharField(max_length=100,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='product',blank=True,null=True)
	price=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id}- {self.product_type_name} {self.enterprise}"

class ServiceType(models.Model):
	'''This model is for service types (eg. drycleaning, petrol wash, darning etc.)'''
	class Meta:
		verbose_name_plural = "Service types"

	id=models.AutoField(primary_key=True)
	
	service_type_name=models.CharField(max_length=100,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='service',blank=True,null=True)
	price=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id}- {self.service_type_name} {self.enterprise}"


class Priority(models.Model):
	'''This model is for priorities(eg. normal,urgent etc.)'''
	class Meta:
		verbose_name_plural = "Priorities"

	id=models.AutoField(primary_key=True)
	
	priority_name=models.CharField(max_length=100,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='priority',blank=True,null=True)
	price=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id}- {self.priority_name} {self.enterprise}"


'''class Rate(models.Model):

	class Meta:
		verbose_name_plural = "Rates"

	id=models.AutoField(primary_key=True)
	price=models.DecimalField(max_digits=6,decimal_places=2,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='rate',blank=True,null=True)
	product=models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='rate',blank=True,null=True)
	service=models.ForeignKey(ServiceType,on_delete=models.CASCADE,related_name='rate',blank=True,null=True)
	priority=models.ForeignKey(Priority,on_delete=models.CASCADE,related_name='rate',blank=True,null=True)

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id}  {self.product} {self.service} {self.priority} {self.price} {self.enterprise}"'''

class PaymentModes(models.Model):
	'''This model is for payment modes(eg. credit card, cash, UPI etc.)'''
	class Meta:
		verbose_name_plural="Payment modes"

	id=models.AutoField(primary_key=True)
	payment_mode_name=models.CharField(max_length=50)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='payment_mode',null=True,blank=True)
	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id}  {self.payment_mode_name}"

class Status(models.Model):
	'''This model is for statuses (eg. Collected at workshop, sent to wash at workshop , delivered to customer etc.)'''
	class Meta:
		verbose_name_plural="Status"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='status',null=True,blank=True)
	status_name=models.CharField(max_length=100)

	def __str__(self):
		return f"{self.id} {self.status_name}"
		


