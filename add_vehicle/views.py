from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vehicle
from .serializers import VehicleSerializer
from .utils import get_edvla_renewal_date, get_insurance_renewal_date

class AddVehicleAPIView(APIView):
    def post(self, request):
        chassis_number = request.data.get('chassis_number')
        libre_number = request.data.get('libre_number')

        edvla_renewal_date = get_edvla_renewal_date(chassis_number)
        if edvla_renewal_date:
            insurance_renewal_date = get_insurance_renewal_date(chassis_number)

            if insurance_renewal_date:
                vehicle, created = Vehicle.objects.update_or_create(
                    chassis_number=chassis_number,
                    defaults={
                        'libre_number': libre_number,
                        'edvla_renewal_date': edvla_renewal_date,
                        'insurance_renewal_date': insurance_renewal_date
                    }
                )

                serializer = VehicleSerializer(vehicle)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Vehicle not found in the insurance company's database", status=status.HTTP_404_NOT_FOUND)

        else:
            return Response("Vehicle not found in the edvla's database", status=status.HTTP_404_NOT_FOUND)
