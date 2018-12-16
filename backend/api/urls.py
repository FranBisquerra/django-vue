from django.contrib import admin
from django.urls import path

from .views import Forecast, Cities

urlpatterns = [

    path('api/forecast', Forecast.as_view(), name='weather_forecast'),

    path('api/cities', Cities.as_view(), name='cities')
]
