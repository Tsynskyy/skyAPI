from rest_framework import serializers
import re


class CitySerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)

    def validate_city(self, value):
        # Проверка ввода на валидность
        if not re.match(r'^[a-zA-Z\s\-]+$', value):
            raise serializers.ValidationError("City name can only contain letters, spaces, and hyphens.")
        return value.strip()
