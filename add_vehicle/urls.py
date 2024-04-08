
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet

router = DefaultRouter()

router.register(r'vehicles', VehicleViewSet, basename='vehicle')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('add_vehicle/', VehicleViewSet.as_view(), name='add_vehicle'),
# ]
