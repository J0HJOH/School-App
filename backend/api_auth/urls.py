from django.urls import path
from .views import (
    UserCreateView,
    UserDestoryView,
    UserUpdateView,
    UserListView,
    UserRetriveView,
    createView,
    MyTokenObtainPairView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
    path('user/update/<int:id>', UserUpdateView.as_view()),
    path('user/delete/<int:id>', UserDestoryView.as_view()),
    path('user/retrive/<int:id>', UserRetriveView.as_view()),
    path('user/list/', UserListView.as_view()),
    path('created', createView),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]