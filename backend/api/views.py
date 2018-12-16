from rest_framework import status
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .constants import Constants
from .serializers import WeatherForecastSerializer

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class Forecast(APIView):

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        payload = {'city': request.query_params.get('city', None)}
        endpoint = 'http://api.openweathermap.org/data/2.5/weather'
        weather_forecast_serializer = WeatherForecastSerializer(data=payload)
        if weather_forecast_serializer.is_valid():
            payload = {'q': request.GET['city'],
                       'APPID': '4961dccab5c36104509ed9351997ba13'}
            response = requests.get(endpoint, payload)
            geodata = response.json()
            return Response(geodata)
        else:
            return Response(weather_forecast_serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class Cities(APIView):

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        return Response(Constants.CITIES)
