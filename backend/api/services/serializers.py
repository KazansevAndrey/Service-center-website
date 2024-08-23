from rest_framework import serializers
from .models import Service, ServiceCategory

class ServicesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = '__all__'

class ServicesCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceCategory
        fields = '__all__'