from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-cities/', views.get_cities, name='get_cities'),
    path('get-weather/', views.get_weather, name='get_weather'),
]
