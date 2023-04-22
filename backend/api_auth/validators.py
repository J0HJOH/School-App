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
    email = User.objects.filter(email__exact = value)
    if value.endswith('edu'):
        raise serializers.ValidationError('Your Email address should not end with edu')
    if email.exists():
        raise serializers.ValidationError("An account has already been created with this email")
    return value

def validate_password(value):
    if len(value) < 8:
        raise serializers.ValidationError('Password must be 8 digits long')
    return value
    
def validate_email_update(value):
    email = User.objects.filter(email__exact = value)
    if value.endswith('edu'):
        raise serializers.ValidationError('Your Email address should not end with edu')
    # if email.exists():
    #     raise serializers.ValidationError("An account has already been created with this email")
    return value

def validate_name_update(value):
    name = User.objects.filter(name__iexact = value)
    # if name.exists():
    #     raise serializers.ValidationError('Name must be unique')
    return value