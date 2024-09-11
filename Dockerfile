FROM python:3.11-slim

# Переменная окружения для работы Docker
ENV PYTHONUNBUFFERED=1

# Рабочая директория в контейнере
WORKDIR /app

# Файл зависимостей в контейнер
COPY requirements.txt /app/

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта в контейнер
COPY . /app/

# Миграции и запуск сервера при старте контейнера
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
