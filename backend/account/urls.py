from django.urls import path
from django.views.generic import TemplateView
from .views import Register, loginView

app_name = "account"

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'), name="home"),
    path('register/', Register, name='signup'),
    path("login", loginView, name = "signin")
]