from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

def validate_name(value):
    name = User.objects.filter(name__iexact = value)
    if name.exists():
        raise serializers.ValidationError('Name must be unique')
    return value

def validate_email(value):
    if value.endswith('edu'):
        raise serializers.ValidationError('Your Email address should not end with edu')
    return value

def validate_password(value):
    try:
        validate_password(value)
        return value
    except Exception as e:
        raise serializers.ValidationError(e)
    
