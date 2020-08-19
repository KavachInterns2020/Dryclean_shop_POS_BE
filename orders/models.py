from django.db import models
from users.managers import CustomUserManager
from enterprise.models import Enterprise
from customers.models import Customer
from employees.models import Employee
from settings.models import ProductType,ServiceType,Priority,Rate,Status
# Create your models here.

class Order(models.Model):

	class Meta:
		verbose_name_plural = "Orders"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
	employee=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
	collection_date=models.DateField()
	expected_delivery_date=models.DateField()
	actual_delivery_date=models.DateField()
	pickup_date=models.DateField()
	total_amount=models.IntegerField()
	
	

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise}"


class OrderItem(models.Model):

	class Meta:
		verbose_name_plural = "Order Items"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	employee=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	product_type=models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	service_type=models.ForeignKey(ServiceType,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	priority=models.ForeignKey(Priority,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	rate=models.ForeignKey(Rate,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	
	quantity=models.IntegerField()
	collection_date=models.DateField()
	expected_delivery_date=models.DateField()
	actual_delivery_date=models.DateField()
	pickup_date=models.DateField()
	total_amount=models.IntegerField()
	
	

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise}"

class StatusHistory(models.Model):

	class Meta:
		verbose_name_plural = "Status History"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	order_item=models.ForeignKey(OrderItem,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	status=models.ForeignKey(Status,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	quantity=models.IntegerField()
	date_of_update=models.DateField()

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise}"
