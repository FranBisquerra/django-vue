from rest_framework import serializers
from .constants import Constants


class WeatherForecastSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)

    def validate_city(self, value):
        if value not in Constants.CITIES:
            raise serializers.ValidationError(
                "The selected city is not available")
        return value