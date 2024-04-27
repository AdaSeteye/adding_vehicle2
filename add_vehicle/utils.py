import requests


def get_edvla_renewal_date(chassis_number):
    api_url = f'https://g-notify-third-parties-1160918eed04.herokuapp.com/vehicle/roadauthrity/{chassis_number}/'
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        vehicle = response.json()
        
        plate_number = vehicle.get('plate_number')
        
        return plate_number
        
    else:
        print(f"Failed to retrieve data from the API. Status code: {response.status_code}")
        return None





def get_insurance_renewal_date(chassis_number):
    insurance_api_url = 'http://127.0.0.1:8001'  

    response = requests.get(f"{insurance_api_url}/renewal_date/{chassis_number}")
    
    if response.status_code == 200:
        renewal_date = response.json()
        return renewal_date
    else:
        return None  
   



