from django.db import models
from users.managers import CustomUserManager
from enterprise.models import Enterprise
from customers.models import Customer
from employees.models import Employee
from settings.models import ProductType,ServiceType,Priority,Status
from workshops.models import Workshop
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

class Order(models.Model):
	'''This models is for details regarding the orders taken by the drycleaner'''
	class Meta:
		verbose_name_plural = "Orders"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
	#employee=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='order',blank=True,null=True)
	
	
	advance_amount=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
	
	#Total amount is calculated in the total_amount function and updated as more order items are added to the order
	@property
	def total_amount(self):
		total=0
		order_item_list=list(OrderItem.objects.all())
		for x in order_item_list:
			if x.order.id== self.id:
				total+=x.total_amount
		

		return total
	#Pending amount is calculated and updated as customer keeps paying advance amount or pays in installments
	@property
	def pending_amount(self):
		if self.total_amount!=0:
			pending=self.total_amount-self.advance_amount
		else:
			pending=0.00
		

		return pending
	
	

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise}"


class OrderItem(models.Model):
	'''This model is for the order items within each order'''
	class Meta:
		verbose_name_plural = "Order Items"

	id=models.AutoField(primary_key=True)
	order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	
	product_type=models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	service_type=models.ForeignKey(ServiceType,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	priority=models.ForeignKey(Priority,on_delete=models.CASCADE,related_name='orderitem',blank=True,null=True)
	
	
	quantity=models.IntegerField(blank=True,null=True)
	collection_date=models.DateField()
	expected_delivery_date=models.DateField()
	actual_delivery_date=models.DateField(blank=True,null=True)
	pickup_date=models.DateField(blank=True,null=True)
	
	
	

	#Total amount field is calculated and updated as the product type, service type and priority are selected

	@property
	def total_amount(self):
		return (self.product_type.price+ self.service_type.price+ self.priority.price)* self.quantity
	
	
	
	

	objects=CustomUserManager()
	def __str__(self):
		return f"{self.id} {self.enterprise}"

class StatusHistory(models.Model):
	'''This model is for details of the status of the order items i.e. whether the items are received, processing ,delivered etc.'''
	class Meta:
		verbose_name_plural = "Status History"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	order_item=models.ForeignKey(OrderItem,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	status=models.ForeignKey(Status,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	#customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	workshop=models.ForeignKey(Workshop,on_delete=models.CASCADE,related_name='statushistory',blank=True,null=True)
	quantity=models.IntegerField()
	date_of_update=models.DateField()

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise}"

