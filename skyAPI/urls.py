from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from weather import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Ручка для получения токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ручка для обновления токена
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # Ручка для получения OpenAPI (Swagger)
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
    path('api/', include('weather.urls')),  # Подключение маршрутов приложения weather
]
