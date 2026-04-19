import requests
from django.shortcuts import render
from django.http import JsonResponse

# Sample data for Indian states and cities
INDIA_LOCATIONS = {
    "Delhi": {
        "cities": {
            "New Delhi": {"lat": 28.6139, "lon": 77.2090},
            "Old Delhi": {"lat": 28.6507, "lon": 77.2334},
            "Dwarka": {"lat": 28.5921, "lon": 77.0460},
        }
    },
    "Maharashtra": {
        "cities": {
            "Mumbai": {"lat": 19.0760, "lon": 72.8777},
            "Pune": {"lat": 18.5204, "lon": 73.8567},
            "Nagpur": {"lat": 21.1458, "lon": 79.0882},
        }
    },
    "Karnataka": {
        "cities": {
            "Bangalore": {"lat": 12.9716, "lon": 77.5946},
            "Mysore": {"lat": 12.2958, "lon": 76.6394},
            "Mangalore": {"lat": 12.9141, "lon": 74.8560},
        }
    },
    "Tamil Nadu": {
        "cities": {
            "Chennai": {"lat": 13.0827, "lon": 80.2707},
            "Coimbatore": {"lat": 11.0168, "lon": 76.9558},
            "Madurai": {"lat": 9.9252, "lon": 78.1198},
        }
    },
    "West Bengal": {
        "cities": {
            "Kolkata": {"lat": 22.5726, "lon": 88.3639},
            "Darjeeling": {"lat": 27.0360, "lon": 88.2627},
            "Siliguri": {"lat": 26.7271, "lon": 88.3953},
        }
    },
    "Rajasthan": {
        "cities": {
            "Jaipur": {"lat": 26.9124, "lon": 75.7873},
            "Udaipur": {"lat": 24.5854, "lon": 73.7125},
            "Jodhpur": {"lat": 26.2389, "lon": 73.0243},
        }
    },
    "Gujarat": {
        "cities": {
            "Ahmedabad": {"lat": 23.0225, "lon": 72.5714},
            "Surat": {"lat": 21.1702, "lon": 72.8311},
            "Vadodara": {"lat": 22.3072, "lon": 73.1812},
        }
    },
    "Kerala": {
        "cities": {
            "Thiruvananthapuram": {"lat": 8.5241, "lon": 76.9366},
            "Kochi": {"lat": 9.9312, "lon": 76.2673},
            "Kozhikode": {"lat": 11.2588, "lon": 75.7804},
        }
    },
}


def index(request):
    """Main page with state and city selection"""
    context = {
        'states': INDIA_LOCATIONS.keys(),
        'weather_data': None
    }
    return render(request, 'index.html', context)


def get_cities(request):
    """AJAX endpoint to get cities for a selected state"""
    state = request.GET.get('state', '')
    if state in INDIA_LOCATIONS:
        cities = list(INDIA_LOCATIONS[state]['cities'].keys())
        return JsonResponse({'cities': cities})
    return JsonResponse({'cities': []})


def get_weather(request):
    """Fetch weather data for selected city"""
    state = request.GET.get('state', '')
    city = request.GET.get('city', '')
    
    if state not in INDIA_LOCATIONS:
        return JsonResponse({'error': 'Invalid state'}, status=400)
    
    if city not in INDIA_LOCATIONS[state]['cities']:
        return JsonResponse({'error': 'Invalid city'}, status=400)
    
    coords = INDIA_LOCATIONS[state]['cities'][city]
    
    # Using OpenWeatherMap API (you need to sign up for a free API key)
    API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'  # Replace with your API key
    
    try:
        # Fetch weather data
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={coords['lat']}&lon={coords['lon']}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            weather_info = {
                'city': city,
                'state': state,
                'temperature': round(data['main']['temp']),
                'feels_like': round(data['main']['feels_like']),
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'].title(),
                'icon': data['weather'][0]['icon'],
                'wind_speed': round(data['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
                'visibility': round(data.get('visibility', 0) / 1000, 1),  # Convert to km
            }
            
            return JsonResponse(weather_info)
        else:
            return JsonResponse({'error': 'Unable to fetch weather data'}, status=500)
            
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'API request failed: {str(e)}'}, status=500)
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)
