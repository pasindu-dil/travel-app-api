from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """Validate the login credentials."""

        email = data["email"]
        password = data["password"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Incorrect email")

        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password")

        data["user"] = user
        return data
    
    def login(self, validated_data):
        """Login and return user object."""
        return validated_data["user"]
