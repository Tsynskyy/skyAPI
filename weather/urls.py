from django.urls import path
from . import views

urlpatterns = [
    # Ручка для получения погоды, обрабатывается в get_weather()
    path('weather/', views.get_weather, name='get_weather'),
]
