from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import (
    validate_email, 
    validate_name,
    validate_password,
    validate_email_update,
    validate_name_update,
)
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

# password = ReadOnlyPasswordHashField()


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [validate_email])
    name = serializers.CharField(validators = [validate_name])
    password = serializers.CharField(validators = [validate_password])
    # confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'password']

    def create(self, validated_data):
        # confirm_password = self.validated_data.pop('email')
        # print(confirm_password)
        return super().create(validated_data)
    
    
    # def validate_confirm_password(self, value):
    #     password = self.validated_data.get('password')
    #     confirm_password = self.validated_data.get("confirm_password")
    #     if password != confirm_password:
    #         raise serializers.ValidationError('The both passwords must be the same')
    #     return value
    
    

class UserUpdateSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [validate_email_update], required = False)
    name = serializers.CharField(validators = [validate_name_update], required = False)
    password = serializers.CharField(validators = [validate_password], required = False)
    department = serializers.CharField(required = False)
    # confirm_password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['name', 'email', 'department', 'password']
    
    def update(self, instance, validated_data):
        name = instance.name
        email = instance.email
        department = instance.department
        updated_name = validated_data.get('name')
        updated_department = validated_data.get('department')
        updated_email = validated_data.get('email')
        
        if not updated_name:
            updated_name = name
        if not updated_email:
            updated_email = email
        if not updated_department:
            updated_department = department
        instance.name = updated_name
        instance.email = updated_email
        instance.department = updated_department
        return super().update(instance, validated_data)