from dataclasses import fields
from .models import Celulares
from rest_framework import serializers

class CelularesSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = Celulares
        fields = '__all__'
