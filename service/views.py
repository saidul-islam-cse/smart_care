from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Service
from .import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ServiceView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer