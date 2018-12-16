from rest_framework import status
from django.test import TestCase
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase


class ForecastAPITestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('backend.api.urls')),
    ]

    def test_correct_city(self):
        url = reverse('weather_forecast')
        response = self.client.get(
            url, data={'city': 'London,uk'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_city(self):
        url = reverse('weather_forecast')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_city(self):
        url = reverse('weather_forecast')
        response = self.client.get(
            url, data={'city': 'Palma,es'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cities(self):
        url = reverse('cities')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
