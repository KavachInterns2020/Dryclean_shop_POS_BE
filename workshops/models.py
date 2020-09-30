from django.db import models
from enterprise.models import Enterprise
from users.models import CustomUser
from users.managers import CustomUserManager

# Create your models here.
class Workshop(models.Model):
	'''Stores details of workshops related to the drycleanshop'''
	class Meta:
		verbose_name_plural='Workshops'

	id=models.AutoField(primary_key=True)
	
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='workshop')
	workshop_name=models.CharField(max_length=200,null=True,blank=True)
	workshop_address=models.CharField(max_length=400,null=True,blank=True)
	workshop_phone=models.CharField(max_length=13,default='+919999999999')
	workshop_email=models.EmailField(null=True,blank=True)

	objects = CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.workshop_name} {self.enterprise}" 