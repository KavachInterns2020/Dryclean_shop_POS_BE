from django.db import models
from users.managers import CustomUserManager
from users.models import CustomUser
from orders.models import Order
from enterprise.models import Enterprise
from settings.models import PaymentModes
# Create your models here.
class Payments(models.Model):
	'''This model holds details of all the monetary transactions of the drycleaning shop'''
	id=models.AutoField(primary_key=True)
	payment_mode=models.ForeignKey(PaymentModes,on_delete=models.CASCADE,related_name='payment',null=True,blank=True)
	order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='payment',null=True,blank=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='payment',null=True,blank=True)
	
	#The amount field is filled automatically when the drycleaner selects an order whose monetary details need to be filled
	@property
	def amount(self):
		amount=self.order.total_amount
		return amount
	
	objects = CustomUserManager()


	def __str__(self):
		return f"{self.id} {self.enterprise} {self.amount}"