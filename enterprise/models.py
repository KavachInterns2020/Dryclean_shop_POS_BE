from django.db import models
from users.managers import CustomUserManager
from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

class Enterprise(models.Model):
	'''This model acts as a profile for the registered user i.e. drycleaner'''
	id=models.AutoField(primary_key=True)
	user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='enterprise')
	contact_name=models.CharField(max_length=200)
	phone=models.CharField(max_length=10)
	shop_name=models.CharField(max_length=200)
	gst_number=models.CharField(max_length=20)
	shop_address=models.CharField(max_length=400)
	#shop_photo=models.ImageField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)
	#updated_at = models.DateTimeField(auto_now_add=True)
	objects = CustomUserManager()

	def __str__(self):
		return str(self.id)

#the post_save signal creates a new enterprise object (i.e. new row in Enterprise table in DB)after a new user is registered
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
	#When a new user is created, the details provided in the registration form are entered into the Enterprise table 
	if created:
		Enterprise.objects.create(user=instance,contact_name=instance.contact_name,
			phone=instance.phone,shop_name=instance.shop_name,gst_number=instance.gst_number,
			shop_address=instance.shop_address)


#The user profile is saved 
@receiver(post_save,sender=CustomUser)
def save_profile(sender,instance,**kwargs):
	try:
		instance.enterprise.save()
	except ObjectDoesNotExist:
		Enterprise.objects.create(user=instance)




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