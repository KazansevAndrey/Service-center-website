
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from applications.models import Application, DeviceType

    
class ApplicationEmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Application
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'client': {'read_only': True},
            'description': {'read_only': True},
            'time_create': {'read_only': True},
            'device': {'read_only': True}
        }

class DeviceTypesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceType()
        fields = '__all__'


class ApplicationClientSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', read_only=True)
    device_title = serializers.SlugRelatedField(source='device', slug_field='device_type', read_only=True)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Application
        fields = ['description', 'device', 'device_title', 'time_create', 'time_update', 'status']
        extra_kwargs = {
            'time_create': {'read_only': True},
            'time_update': {'read_only': True},
            'status': {'read_only': True},
            'device_title': {'read_only': True}
        }
    
 