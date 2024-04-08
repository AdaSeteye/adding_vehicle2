
from rest_framework import viewsets, status
from rest_framework.response import Response
from .utils import get_vehicle_info_from_insurance
from .serializers import VehicleSerializer

class VehicleViewSet(viewsets.ViewSet):
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            chassis_number = serializer.validated_data.get('chassis_number')
            # libre_number = serializer.validated_data.get('libre_number')
            
            # renewal_date_institution = get_vehicle_info_from_institution(chassis_number)
            # if renewal_date_institution is None:
            #     return Response({"error": "Vehicle not found in institution database."}, status=status.HTTP_404_NOT_FOUND)
            
            renewal_date_insurance = get_vehicle_info_from_insurance(chassis_number)
            if renewal_date_insurance is None:
                return Response({"error": "Vehicle not found in insurance company database."}, status=status.HTTP_404_NOT_FOUND)
            
            vehicle_data = {
                'chassis_number': chassis_number,
                # 'libre_number': libre_number,
                # 'institution_document_renewal_date': renewal_date_institution,
                'insurance_document_renewal_date': renewal_date_insurance
            }
            serializer = VehicleSerializer(data=vehicle_data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Vehicle added successfully."}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
