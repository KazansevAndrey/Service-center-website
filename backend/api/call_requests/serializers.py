from dataclasses import field, fields
from rest_framework import serializers
from .models import CallRequest
class CallRequestSerializer(serializers.ModelSerializer):
    '''Сериализатор заявок на звонки'''
    class Meta:
        model = CallRequest
        fields = '__all__'
