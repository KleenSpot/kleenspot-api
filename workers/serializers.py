from rest_framework import serializers
from .models.Cleaners import Cleaner
from .models.Services import Service

class CleanerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cleaner
        fields = ['name', 'phone', 'address', 'city']


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['name', 'description']
