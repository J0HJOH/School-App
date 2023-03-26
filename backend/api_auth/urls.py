from django.urls import path
from .views import (
    UserCreateView,
    UserDestoryView,
    UserUpdateView,
    UserListView,
    UserRetriveView
)

urlpatterns = [
    path('create/', UserCreateView.as_view()),
    path('update/', UserUpdateView.as_view()),
    path('delete/', UserDestoryView.as_view()),
    path('retrive/', UserRetriveView.as_view()),
    path('list/', UserListView.as_view())
]