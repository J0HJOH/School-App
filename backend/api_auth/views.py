from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import (
    DestroyAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from .serializers import UserSerializers, UserUpdateSerializers
from rest_framework import permissions, authentication
from .permissions import UserPerm
from .authentication import TokenAuthentication
from rest_framework_api_key.permissions import HasAPIKey

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.


User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        token['department'] = user.department

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# CLASS-BASED API view for account creation 
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

        

# list all the users 
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

# Update user detalis
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_update(self, serializer):
        instance = serializer.save()

        password = instance.password
      
        updated_password = serializer.validated_data.get('password')
       
        if not updated_password:
            updated_password = password
            instance.set_password(updated_password)
            instance.save()
        if updated_password:
            instance.set_password(updated_password)
            instance.save()
        
        
# delete users
class UserDestoryView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

# obtain a single user
class UserRetriveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

@api_view(['GET', 'POST'])
def createView(request, *args, **kwargs):
    method = request.method
    if method == 'GET':
        queryset = User.objects.all()
        data = UserSerializers(queryset, many = True)
        return Response(data.data)

    if method == 'POST':
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data, status_code = 200)
        return Response(serializer)