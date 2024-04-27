
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AddVehicleAPIView


urlpatterns = [
    path('add_vehicle/', AddVehicleAPIView.as_view(), name='add_vehicle'),
]
