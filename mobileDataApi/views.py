# Create your views here.

from django.shortcuts import render
from rest_framework import generics
from .serializers import BusDatalistSerializer
from .models import BusDatalist

class CreateView(generics.ListCreateAPIView):

	queryset = BusDatalist.objects.all()
	serializer_class = BusDatalistSerializer

	def perform_create(self, serializer):

		serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

	queryset = BusDatalist.objects.all()
	serializer_class = BusDatalistSerializer