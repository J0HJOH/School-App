from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import validate_email, validate_name
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

# password = ReadOnlyPasswordHashField()


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [validate_email])
    name = serializers.CharField(validators = [validate_name])
    # password = serializers.CharField()
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

