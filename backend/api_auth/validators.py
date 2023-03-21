from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

def validate_name(value):
    name = User.objects.filter(name__iexact = value)
    if name.exists():
        return serializers.ValidationError('Name must be unique')
    return value

def validate_email(value):
    if value.endswith('edu'):
        return serializers.ValidationError('Your Email address should not end with edu')
    return value