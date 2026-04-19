from django.contrib import admin
from .models import WeatherQuery

@admin.register(WeatherQuery)
class WeatherQueryAdmin(admin.ModelAdmin):
    list_display = ['city', 'state', 'queried_at']
    list_filter = ['state', 'queried_at']
    search_fields = ['city', 'state']
