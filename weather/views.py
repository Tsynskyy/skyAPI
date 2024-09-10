from django.shortcuts import render

import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from requests.exceptions import RequestException, ConnectionError, Timeout


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_weather(request):
    city = request.query_params.get('city')

    if not city:
        return Response({"error": "City is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Проверка кеша
    cached_weather = cache.get(city)
    if cached_weather:
        print("Returning cached data for:", city)
        return Response(cached_weather)

    try:
        api_key = settings.OPENWEATHER_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(url, timeout=5)  # Таймаут на случай долгих запросов
            response.raise_for_status()  # Ошибка, если статус не 2xx

            data = response.json()
            cache.set(city, data, timeout=1800)  # Кеш на 30 минут
            print("Caching data for:", city)  # Лог кеша
            return Response(data)

        except (ConnectionError, Timeout, RequestException) as e:
            print(f"OpenWeather is unavailable: {e}. Switching to the backup WeatherAPI")
            api_key_backup = settings.WEATHERAPI_KEY
            backup_url = f'http://api.weatherapi.com/v1/current.json?q={city}&key={api_key_backup}'

            # Таймаут для резервного API
            backup_response = requests.get(backup_url, timeout=5)
            backup_response.raise_for_status()

            data = backup_response.json()
            cache.set(city, data, timeout=1800)  # Кеш на 30 минут
            return Response(data)

    except (ConnectionError, Timeout, RequestException) as e:

        return Response({"error": f"Both weather providers are unavailable: {e}"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
