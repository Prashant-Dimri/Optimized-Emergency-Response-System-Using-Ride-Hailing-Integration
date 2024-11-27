import math
from django.shortcuts import render

ambulance_locations = [
    {"name": "Clock Tower", "lat": 30.3165, "lon": 78.0322},
    {"name": "Rajpur Road", "lat": 30.3065, "lon": 78.0295},
    {"name": "Kashmir Basti", "lat": 30.3160, "lon": 78.0463},
    {"name": "Mussoorie Road", "lat": 30.3250, "lon": 78.0895},
    {"name": "Paltan Bazaar", "lat": 30.3130, "lon": 78.0321},
    {"name": "Dehradun Road", "lat": 30.3045, "lon": 78.0709},
    {"name": "Vikasnagar", "lat": 30.2875, "lon": 78.0986},
    {"name": "Selakui", "lat": 30.2760, "lon": 78.0968},
    {"name": "Doon Hospital", "lat": 30.3155, "lon": 78.0329},
    {"name": "Malsi Forest", "lat": 30.3195, "lon": 78.1231},
]

ride_hailing_services = [
    {"name": "Indira Market", "lat": 30.3100, "lon": 78.0320},
    {"name": "Haridwar Bypass", "lat": 30.3115, "lon": 78.0270},
    {"name": "Doon IT Park", "lat": 30.3185, "lon": 78.0840},
    {"name": "Kempty Falls", "lat": 30.4589, "lon": 78.2351},
    {"name": "Mussoorie Mall Road", "lat": 30.4534, "lon": 78.1226},
    {"name": "Patel Nagar", "lat": 30.3200, "lon": 78.0425},
    {"name": "Ajabpur Kalan", "lat": 30.3075, "lon": 78.0545},
    {"name": "Sahastradhara", "lat": 30.3175, "lon": 78.1010},
    {"name": "Chandrabani", "lat": 30.3075, "lon": 78.1225},
    {"name": "Rajaji National Park", "lat": 30.1360, "lon": 78.1875},
]

def haversine(lat1, lon1, lat2, lon2):

    R = 6371  # Radius of the Earth in kilometers

    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # Distance in kilometers

    return distance

def find_nearest_location(user_lat, user_lon, locations):
    
    nearest_location = None
    min_distance = float('inf')

    for location in locations:
        distance = haversine(user_lat, user_lon, location['lat'], location['lon'])
        if distance < min_distance:
            min_distance = distance
            nearest_location = location

    return nearest_location
def home(request):
    return render(request, 'home.html')
def get_location(request):
    return render(request, 'get_location.html')

def send_location(request):
    if request.method == 'POST':
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))

        if latitude and longitude:

            nearest_ambulance = find_nearest_location(latitude, longitude, ambulance_locations)

            nearest_ola = find_nearest_location(latitude, longitude, ride_hailing_services)

            meeting_point = "F.R.I"

            return render(request, 'get_location.html', {
                'nearest_ambulance': nearest_ambulance['name'],
                'nearest_ola': nearest_ola['name'],
                'meeting_point': meeting_point,
            })
    return render(request, 'get_location.html', {'error': 'Location not found or invalid.'})
