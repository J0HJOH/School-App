from django.urls import path
from .views import (
    UserCreateView,
    UserDestoryView,
    UserUpdateView,
    UserListView,
    UserRetriveView,
    createView,
    MyTokenObtainPairView,
    create_api_keyViews
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken import views

app_name = 'api'
urlpatterns = [
    path('user/create/', UserCreateView.as_view(), name='create'),
    path('user/update/<int:id>/', UserUpdateView.as_view(), name='update'),
    path('user/delete/<int:id>/', UserDestoryView.as_view(), name='delete'),
    path('user/retrive/<int:id>/', UserRetriveView.as_view(), name='retrive'),
    path('user/list/', UserListView.as_view(), name='list'),
    path('created/', createView),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create-keys/', create_api_keyViews, name='create-keys'),

]

urlpatterns += [
    path('obtain-token/', views.obtain_auth_token)
]