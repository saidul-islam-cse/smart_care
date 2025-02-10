from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .import models
from .import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class AppointmentView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializers

    def get_queryset(self):
        queryset = super().get_queryset()

        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset