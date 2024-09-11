
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from applications.models import Application, DeviceType

# Заявки которые в данный момент выполняются 
class EmployeeEmailApplicationSerializer(serializers.ModelSerializer):
    employee_email = serializers.SlugRelatedField(source='employee', slug_field='user__email', read_only=True)
    class Meta:
        model = Application
        fields = ('id', 'employee_email','time_create')

# Персональные заявки
class ClientEmailApplicationSerializer(serializers.ModelSerializer):
    user_email = serializers.SlugRelatedField(source='client', slug_field='email', read_only=True)
    class Meta:
        model = Application
        fields = ('id', 'user_email', 'time_create')
        

class DeviceTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ('id', 'device_type')

class ApplicationRetriveSerializer(serializers.ModelSerializer):
    user_email = serializers.SlugRelatedField(source='client', slug_field='email', read_only=True)
    user_first_name = serializers.SlugRelatedField(source='client', slug_field='first_name', read_only=True)
    user_last_name = serializers.SlugRelatedField(source='client', slug_field='last_name', read_only=True)
    user_phone_number = serializers.SlugRelatedField(source='client', slug_field='phone_number', read_only=True)
    status_title = serializers.CharField(source='get_status_display', read_only=True)
    device_title = serializers.SlugRelatedField(source='device', slug_field='device_type', read_only=True)
    employee_id = serializers.SlugRelatedField(source='employee', slug_field='user__id', read_only=True)

    class Meta:
        model = Application
        fields = ('id', 'user_email', 'user_first_name', 'user_last_name', 'user_phone_number', 'status_title', 'device_title', 'description', 'time_create', 'employee_id', 'is_archived')
        extra_kwargs={
            'description': {'read_only': True}
        }


class ApplicationClientSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', read_only=True)
    device_title = serializers.SlugRelatedField(source='device', slug_field='device_type', read_only=True)
    user_email = serializers.SlugRelatedField(source='client', slug_field='email', read_only=True)

    class Meta:
        model = Application
        fields = ('id','device', 'user_email', 'description', 'device_title', 'time_update', 'status', 'time_create')
        extra_kwargs = {
            'time_create': {'read_only': True},
            'time_update': {'read_only': True},
            'status': {'read_only': True},
            'device_title': {'read_only': True}
        }
    
