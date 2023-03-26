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
# Create your views here.

User = get_user_model()


# CLASS-BASED API view for account creation 
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPerm]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_create(self, serializer):
        return super().perform_create(serializer)

# list all the users 
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPerm]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

# Update user detalis
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPerm]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_update(self, serializer):
        return super().perform_update(serializer)

# delete users
class UserDestoryView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPerm]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

# obtain a single user
class UserRetriveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, UserPerm]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]