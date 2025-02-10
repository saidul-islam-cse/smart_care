from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .import views
router.register('list', views.DoctorView)
router.register('specialization', views.SpecializationView)
router.register('designation', views.DesignationView)
router.register('available_time', views.AvailableTimeView)
router.register('review', views.ReviewView)
urlpatterns = [
    path('', include(router.urls))
]