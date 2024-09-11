# skyAPI


## Настройка проекта

Для запуска проекта необходимо зарегистрироваться на следующих сайтах и получить API ключи:

1. **OpenWeather API**: 
   - [OpenWeather](https://home.openweathermap.org/users/sign_up)
2. **WeatherAPI**:
   - [WeatherAPI](https://www.weatherapi.com/signup.aspx)

### Конфигурация .env файла

После получения ключей необходимо создать файл `.env` в корне проекта и добавить в него следующие строки:

```bash
OPENWEATHER_API_KEY=ваш_openweather_api_ключ
WEATHERAPI_KEY=ваш_weatherapi_ключ
SECRET_KEY=ваш_django_secret_key
