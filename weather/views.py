from django.shortcuts import render

import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_weather(request):
    city = request.query_params.get('city')

    if not city:
        return Response({"error": "City parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

    # Проверяем кеш
    cached_weather = cache.get(city)
    if cached_weather:
        return Response(cached_weather)

    try:
        api_key = settings.OPENWEATHER_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            cache.set(city, data, timeout=1800)  # Кешируем на 30 минут
            return Response(data)
        else:
            return Response({"error": "Unable to get weather data"}, status=response.status_code)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
