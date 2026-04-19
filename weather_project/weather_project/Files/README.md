# 🌤️ Weather Dashboard - Django Project

A modern, responsive weather application built with Django, HTML, and CSS. Get real-time weather information for cities across India.

## Features

- 🗺️ **State & City Selection**: Interactive dropdowns for selecting Indian states and cities
- 🌡️ **Real-time Weather Data**: Temperature, humidity, wind speed, pressure, and visibility
- 📱 **Responsive Design**: Works perfectly on desktop and mobile devices
- 🎨 **Beautiful UI**: Modern gradient design with smooth animations
- ⚡ **AJAX Integration**: Dynamic city loading without page refresh
- 🌈 **Weather Icons**: Emoji-based weather condition indicators

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

### 1. Clone or Download the Project

Download this project to your local machine.

### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Get OpenWeatherMap API Key

1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Navigate to API keys section
4. Copy your API key
5. Open `weather_app/views.py`
6. Replace `'YOUR_OPENWEATHERMAP_API_KEY'` with your actual API key:

```python
API_KEY = 'your_actual_api_key_here'
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional - for admin access)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

Open your browser and go to:
- **Main App**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/ (if you created a superuser)

## Project Structure

```
weather_project/
├── weather_app/
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── models.py         # Database models
│   ├── urls.py           # App URL patterns
│   └── views.py          # View functions with weather logic
├── templates/
│   └── index.html        # Main HTML template with CSS & JS
├── manage.py             # Django management script
├── settings.py           # Django settings
├── urls.py               # Project URL configuration
├── wsgi.py               # WSGI configuration
└── requirements.txt      # Python dependencies
```

## How It Works

1. **State Selection**: User selects a state from the dropdown
2. **City Loading**: Cities are dynamically loaded via AJAX
3. **Weather Fetch**: Clicking "Get Weather" fetches data from OpenWeatherMap API
4. **Display**: Weather information is beautifully displayed with icons and details

## Available States & Cities

The application includes 8 major Indian states with multiple cities:
- **Delhi**: New Delhi, Old Delhi, Dwarka
- **Maharashtra**: Mumbai, Pune, Nagpur
- **Karnataka**: Bangalore, Mysore, Mangalore
- **Tamil Nadu**: Chennai, Coimbatore, Madurai
- **West Bengal**: Kolkata, Darjeeling, Siliguri
- **Rajasthan**: Jaipur, Udaipur, Jodhpur
- **Gujarat**: Ahmedabad, Surat, Vadodara
- **Kerala**: Thiruvananthapuram, Kochi, Kozhikode

## Customization

### Adding More States/Cities

Edit `weather_app/views.py` and add entries to the `INDIA_LOCATIONS` dictionary:

```python
INDIA_LOCATIONS = {
    "New State": {
        "cities": {
            "City Name": {"lat": latitude, "lon": longitude},
        }
    }
}
```

### Changing Colors/Design

Edit the `<style>` section in `templates/index.html` to customize:
- Background gradient
- Card colors
- Button styles
- Typography

## API Information

This project uses the OpenWeatherMap API:
- **Free Tier**: 1,000 API calls/day
- **Data Includes**: Temperature, humidity, pressure, wind speed, visibility, weather conditions
- **Documentation**: https://openweathermap.org/current

## Troubleshooting

### "Invalid API Key" Error
- Ensure you've replaced `YOUR_OPENWEATHERMAP_API_KEY` in `views.py`
- Verify your API key is active on OpenWeatherMap

### Cities Not Loading
- Check your internet connection
- Ensure Django development server is running
- Check browser console for JavaScript errors

### Weather Data Not Displaying
- Verify API key is correct
- Check if you've exceeded free tier limit (1000 calls/day)
- Check browser network tab for API response

## Technologies Used

- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **API**: OpenWeatherMap API
- **HTTP Client**: Python Requests library

## Features Explained

### Temperature Display
- Shows current temperature in Celsius
- "Feels like" temperature for better accuracy

### Weather Details
- **Humidity**: Percentage of moisture in air
- **Wind Speed**: Converted from m/s to km/h
- **Pressure**: Atmospheric pressure in hPa
- **Visibility**: How far you can see in kilometers

### Responsive Design
- Mobile-first approach
- Adapts to different screen sizes
- Touch-friendly interface

## License

This project is open source and available for educational purposes.

## Contributing

Feel free to fork this project and add:
- More cities and states
- Different weather APIs
- Weather forecasts (5-day, hourly)
- Historical weather data
- Weather maps
- User preferences

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify all setup steps were followed
3. Ensure API key is valid and active

## Credits

- Weather data provided by OpenWeatherMap
- Icons using emoji characters
- Design inspired by modern weather apps

---

**Happy Weather Tracking! 🌤️**
