# skyAPI

skyAPI - это веб-сервис для получения текущей погоды в указанном городе с использованием двух провайдеров погоды (OpenWeather и WeatherAPI). Проект разработан на Django с использованием Django REST Framework и JWT-аутентификации.

## Возможности:
1. **JWT-аутентификация**: реализация ручек для получения и обновления токена.
2. **Кеширование**: запросы на погоду для одного города кешируются на 30 минут.
3. **Отказоустойчивость**: при недоступности основного провайдера (OpenWeather) запрос автоматически перенаправляется на резервного (WeatherAPI).
4. **Swagger (OpenAPI)**: автоматически генерируемая документация для всех доступных API.

## Стек:
- Python
- Django
- Django REST Framework
- djangorestframework-simplejwt для JWT токенов
- drf-spectacular для OpenAPI документации
- Docker для упаковки и развёртывания
- Git и GitHub для контроля версий

## Установка и запуск проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/Tsynskyy/skyAPI.git
cd skyAPI
```

### 2. Настройка переменных окружения

Для работы проекта необходимы API-ключи для двух провайдеров погоды:

- [OpenWeather](https://home.openweathermap.org/users/sign_up)
- [WeatherAPI](https://www.weatherapi.com/signup.aspx)

Создайте файл `.env` в корне проекта и добавьте следующие строки:

```bash
OPENWEATHER_API_KEY=ваш_openweather_api_ключ
WEATHERAPI_KEY=ваш_weatherapi_ключ
SECRET_KEY=ваш_django_secret_key
```

### 3. Запуск с Docker

Для запуска проекта необходимо выполнить команду:

```bash
docker-compose up
```

Приложение будет доступно по адресу: `http://127.0.0.1:8000`

### 4. Доступ к API

1. **Получение токена**:  
   POST `http://127.0.0.1:8000/api/token/`  
   Параметры:
   - `username`
   - `password`

2. **Обновление токена**:  
   POST `http://127.0.0.1:8000/api/token/refresh/`  
   Параметры:
   - `refresh`

3. **Получение погоды** (требуется JWT токен):  
   GET `http://127.0.0.1:8000/api/weather/?city=название_города`  
   Параметры:
   - `city`: название города

### 5. Swagger (OpenAPI)

Документация к API доступна по адресу:  
`http://127.0.0.1:8000/api/docs/`
