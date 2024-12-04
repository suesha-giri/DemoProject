from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email is already registered.')
        return value
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    login = serializers.CharField()
    class Meta:
        model = User
        fields = ['login', 'password']

    def validate(self, attrs):
        user = User.objects.filter(Q(email=attrs['login']) | Q(username=attrs['login'])).first()
        if not user:
            raise serializers.ValidationError("User does not exist. Please register first.")
        
        auth_user = authenticate(username=user.username, password=attrs['password'])

        if not auth_user:
            raise serializers.ValidationError({"password": "Invalid password."})
        
        attrs['user'] = auth_user
        
        return attrs

