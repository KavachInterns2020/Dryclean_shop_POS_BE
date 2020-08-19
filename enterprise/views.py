from django.shortcuts import render
from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializer,EditProfileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Profile(LoginRequiredMixin,APIView):

	def get_object(self, pk):
	    try:
	        return Enterprise.objects.get(pk=pk)
	    except Enterprise.DoesNotExist:
	        raise Http404

	def get(self, request, pk, format=None):
	    enterprise = self.get_object(pk)
	    serializer = EnterpriseSerializer(enterprise)
	    return Response(serializer.data)

class EditProfile(LoginRequiredMixin,APIView):
	def get_object(self,pk):
		try:
			return Enterprise.objects.get(pk=pk)
		except Enterprise.DoesNotExist:
			raise Http404

	def put(self, request, pk, format=None):
	    enterprise = self.get_object(pk)
	    serializer = EditProfileSerializer(enterprise, data=request.data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response(serializer.data)
	    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


