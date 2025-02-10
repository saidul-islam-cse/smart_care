from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly 

# Create your views here.
from .import models
from .import serializers

class SpecializationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class DesignationView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set


class AvailableTimeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = page_size
    max_page_size = 100

class DoctorView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    pagination_class = DoctorPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'specialization__name', 'designation__name']

class ReviewView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly ]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer