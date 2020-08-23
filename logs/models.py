from django.db import models
from enterprise.models import Enterprise
from users.models import CustomUser
from users.managers import CustomUserManager
# Create your models here.
class Logs(models.Model):

	class Meta:
		verbose_name_plural='Logs'
		
	id=models.AutoField(primary_key=True)
	query=models.CharField(max_length=400)
	user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='log')
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='log')
	timestamp=models.DateTimeField(auto_now_add=True)
	ip_address=models.CharField(max_length=48)

	objects = CustomUserManager()