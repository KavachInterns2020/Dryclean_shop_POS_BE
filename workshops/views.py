from django.shortcuts import render
from workshops.models import Workshop
from workshops.serializers import WorkshopSerializer,WorkshopCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import rest_framework.mixins
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
class WorkshopView(LoginRequiredMixin,APIView):

	def get(self, request, format=None):
		workshop = self.request.user.enterprise.workshop.all()
		serializer = WorkshopSerializer(workshop, many=True)
		return Response(serializer.data)


class WorkshopDetailView(LoginRequiredMixin,APIView):
	def get(self, request,pk,format=None):
		workshop=self.request.user.enterprise.workshop.filter(id=pk)
		serializer = WorkshopSerializer(workshop,many=True)
		return Response(serializer.data)



class WorkshopCreateView(LoginRequiredMixin,generics.CreateAPIView):
	def get_serializer_class(self):
	    if self.request.user.is_authenticated:
	        return WorkshopCreateSerializer
	    return Response(serializer.errors,status=Http404)

	def perform_create(self, serializer, **kwargs):
		
		
		if serializer.is_valid():
			
			serializer.save(enterprise=self.request.user.enterprise)
			
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditWorkshopView(LoginRequiredMixin,UpdateModelMixin,DestroyModelMixin,generics.GenericAPIView):
	def get_queryset(self):
		return self.request.user.enterprise.workshop.all()
	serializer_class = WorkshopCreateSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
