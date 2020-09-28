
from rest_framework import serializers

from users.models import CustomUser
from enterprise.models import Enterprise
from allauth.account.utils import setup_user_email
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer

class UserSerializer(serializers.ModelSerializer):
	'''Overwriting django's in built user serializer to serialize CustomUser model and provode fields id and email'''
	class Meta:
		model = CustomUser
		fields = ['id', 'email']

class CustomRegisterSerializer(RegisterSerializer):
	'''Overwriting rest-auth app's default register serializer to include fields of our choice'''
	contact_name=serializers.CharField(max_length=200,default="none")
	phone=serializers.CharField(max_length=10,default="9999999999")
	shop_name=serializers.CharField(max_length=200,default="none")
	gst_number=serializers.CharField(max_length=20,default="none")
	shop_address=serializers.CharField(max_length=400,default="none")
	#shop_photo=serializers.ImageField(upload_to='images/',null=True)
	
	def get_cleaned_data(self):
	    return{
	    	
	    	'password1':self.validated_data.get('password1', ''),
        	'email':self.validated_data.get('email', ''),
	        'contact_name':self.validated_data.get('contact_name', ''),
	        'phone':self.validated_data.get('phone', ''),
	        'shop_name':self.validated_data.get('shop_name', ''),
	        'gst_number':self.validated_data.get('gst_number', ''),
	        'shop_address':self.validated_data.get('shop_address', '')
	    }

class CustomLoginSerializer(LoginSerializer):
	'''Overwriting rest-auth's default login serializer to display fields of our choice'''
	def get_cleaned_data(self):
		return{
		
		
		'email':self.validated_data.get('email', ''),
		'password':self.validated_data.get('password', ''),

		}