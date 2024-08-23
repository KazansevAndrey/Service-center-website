from django.forms import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    is_employee = serializers.BooleanField(source='employeeprofile')
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'surname', 'phone_number', 'email', 'password', 'is_employee')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)