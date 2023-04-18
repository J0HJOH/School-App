from django.shortcuts import render
from rest_framework.generics import (
    DestroyAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from django.contrib.auth import get_user_model
from .serializers import UserSerializers
from rest_framework import permissions, authentication
from .permissions import UserPerm
from .authentication import TokenAuthentication
from rest_framework_api_key.permissions import HasAPIKey
# Create your views here.

User = get_user_model()


# CLASS-BASED API view for account creation 
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly |UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    # def perform_create(self, serializer):
    #     # password = serializer.validated_data.get('password')
    #     # confirm_password = serializer.validated_data.get('confirm_password')
    #     # if confirm_password == password:
    #     #     password = confirm_password

    #     #     serializer.save(password=password)

    #     return super().perform_create(serializer)

# list all the users 
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

# Update user detalis
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_update(self, serializer):
        return super().perform_update(serializer)

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