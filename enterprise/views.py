from django.shortcuts import render
from enterprise.models import Enterprise
from enterprise.serializers import EnterpriseSerializer,EditProfileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin,ListModelMixin
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
class Profile(LoginRequiredMixin,APIView):
	'''GET, displays the enterprise details'''
	def get(self, request,format=None):
		enterprise_id=self.request.user.enterprise.id
		queryset=Enterprise.objects.filter(id=enterprise_id)
		serializer = EnterpriseSerializer(queryset,many=True)
		return Response(serializer.data)

	

class EditProfile(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	'''PUT,DELETE, to edit or delete enterprise details. Upon deletion all records related to the user are deleted'''
	def get_queryset(self):
		enterprise_id=self.request.user.enterprise.id
		queryset=Enterprise.objects.filter(id=enterprise_id)
		return queryset

	serializer_class=EditProfileSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)


