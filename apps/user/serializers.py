from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'date_joined']
        
        extra_kwargs = {
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'date_joined': {'read_only': True},
        }
    