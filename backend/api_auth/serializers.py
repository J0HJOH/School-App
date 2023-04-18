from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import (
    validate_email, 
    validate_name,
    validate_password,
    
    )
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

# password = ReadOnlyPasswordHashField()


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [validate_email])
    name = serializers.CharField(validators = [validate_name])
    password = serializers.CharField(validators = [validate_password])
    confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'password', 'confirm_password']

    def create(self, validated_data):
        confirm_password = self.validated_data.pop('email')
        print(confirm_password)
        return super().create(validated_data)
    
    # def validate_confirm_password(self, value):
    #     password = self.validated_data.get('password')
    #     confirm_password = self.validated_data.get("confirm_password")
    #     if password != confirm_password:
    #         raise serializers.ValidationError('The both passwords must be the same')
    #     return value
    
    

