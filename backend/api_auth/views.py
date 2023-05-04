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
from django.contrib import messages
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .forms import APIkeyForm
from rest_framework_api_key.models import APIKey
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

    # def get_authenticate_header(self, request):
    #     # return super().get_authenticate_header(request)
    #     print(super().get_authenticate_header(request))
    #     print(request.headers)

    # def test(self):
    #     print(self.request.headers)

    # # def get(self, request, *args, **kwargs):
    # #     # return super().get(request, *args, **kwargs)
    # #     print(request.headers)
    

# Update user detalis
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializers
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly | UserPerm | HasAPIKey]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]

    def perform_update(self, serializer):
        instance = serializer.save()
        print(self.request.headers)

        password = instance.password
        instance.set_password(password)
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
    

def create_api_keyViews(request, *args, **kwargs):
    api_key = ''
    api_name = ''
    user = request.user.name
    user_api_keys = APIKey.objects.filter(name__icontains = user)
    if request.POST:
        name = request.POST.get('api_key_name')
        if name:
            api_name, api_key = APIKey.objects.create_key(name = name)

            messages.success(request, f'The API key for {name}: {api_key}. Please store it somewhere safe: you will not be able to see it again.')
            messages.success(request, f'The API key “{name}” was added successfully.')
    context = {
        'user_api_keys': user_api_keys
    }
    return render(request, 'user/create_api_key.html', context)