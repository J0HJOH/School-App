from django.urls import path
from .views import (
    UserCreateListView,
    UserDestoryView,
    UserRetriveUpdateView
)

urlpatterns = [
    path('list/', UserCreateListView.as_view()),
    path('detail/', UserRetriveUpdateView.as_view()),
    path('delete/', UserDestoryView.as_view())
]