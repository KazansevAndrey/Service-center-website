
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from applications.models import Application, DeviceType

# Заявки которые в данный момент выполняются 
class CurrentRepairApplicationSerializer(serializers.ModelSerializer):
    employee_email = serializers.SlugRelatedField(source='employee', slug_field='user__email', read_only=True)
    class Meta:
        model = Application
        fields = ('id', 'employee_email','time_create')

# Персональные заявки
class RepairApplicationSerializer(serializers.ModelSerializer):
    user_email = serializers.SlugRelatedField(source='client', slug_field='email', read_only=True)
    class Meta:
        model = Application
        fields = ('id', 'user_email', 'time_create')
        

class DeviceTypesSerializer(serializers.ModelSerializer):
    device_title = serializers.SlugRelatedField(source='device', slug_field='device_type', read_only=True)
    user_email = serializers.SlugRelatedField(source='client', slug_field='email', read_only=True)
    class Meta:
        model = DeviceType()
        fields = ('id', 'device_title', 'user_email')


class ApplicationClientSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', read_only=True)
    device_title = serializers.SlugRelatedField(source='device', slug_field='device_type', read_only=True)
    user_email = serializers.SlugRelatedField(source='client', slug_field='email', read_only=True)

    class Meta:
        model = Application
        fields = ('id','device', 'user_email', 'device_title', 'time_update', 'status', 'time_create')
        extra_kwargs = {
            'time_create': {'read_only': True},
            'time_update': {'read_only': True},
            'status': {'read_only': True},
            'device_title': {'read_only': True}
        }
    
 