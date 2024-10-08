from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from django.core.cache import cache
from .serializers import CitySerializer
from .services import WeatherHandler
from requests.exceptions import RequestException, ConnectionError, Timeout


class GetWeatherView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CitySerializer

    def get(self, request):
        serializer = self.get_serializer(data=request.query_params)
        if serializer.is_valid():
            city = serializer.validated_data['city']

            # Проверка кеша
            cached_weather = cache.get(city)
            if cached_weather:
                print("Возврат кэшированных данных для:", city)
                return Response(cached_weather)

            weather_handler = WeatherHandler()
            try:
                try:
                    data = weather_handler.get_weather_main(city)
                except (ConnectionError, Timeout, RequestException) as e:
                    print(f"OpenWeather недоступен: {e}. Переключение на резервный WeatherAPI")
                    data = weather_handler.get_weather_backup(city)
                cache.set(city, data, timeout=1800)  # Кеш на 30 мин
                return Response(data)
            except (ConnectionError, Timeout, RequestException) as e:
                return Response({"Ошибка": f"Оба провайдера недоступны: {e}"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            except Exception as e:
                return Response({"Ошибка": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def home(request):
    return HttpResponse("Домашняя страница skyAPI")
