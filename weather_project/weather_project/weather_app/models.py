from django.db import models

# This project uses hardcoded location data in views.py
# But you can create models here if you want to store locations in database

class WeatherQuery(models.Model):
    """Optional: Track weather queries for analytics"""
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    queried_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-queried_at']
    
    def __str__(self):
        return f"{self.city}, {self.state} - {self.queried_at}"
