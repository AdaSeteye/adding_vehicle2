import requests
from .models import Vehicle
# from .views import ListVehiclesApiViewSet

# def get_vehicle_info_from_institution(chassis_number):
#     api_view = ListVehiclesApiViewSet()
#     response = api_view.retrieve(request=None, chassis_number=chassis_number)
    
#     if response.status_code == 404:
#         return None, None  
    
#     institution_data = response.data
#     renewal_date = institution_data.get('institution_document_renewal_date')
    
#     return renewal_date


def get_vehicle_info_from_insurance(chassis_number):
    insurance_api_url = 'http://127.0.0.1:8001'  
    response = requests.get(f"{insurance_api_url}/renewal_date/{chassis_number}")
    
    if response.status_code == 200:
        renewal_date = response.json()
        return renewal_date
    else:
        return None  
   


# def add_vehicle(chassis_number, renewal_date_institution, renewal_date_insurance):
#     vehicle, created = Vehicle.objects.update_or_create(
#         chassis_number=chassis_number,
#         defaults={
#             'institution_document_renewal_date': renewal_date_institution,
#             'insurance_document_renewal_date': renewal_date_insurance
#         }
#     )
#     return created 
