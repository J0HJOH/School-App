from django.urls import path
from django.views.generic import TemplateView
from .views import Register, loginView, apiDocs
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name = "account"

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'index.html'), name="home"),
    path('register/', Register, name='signup'),
    path("login", loginView, name = "signin"),
    path('user/dashboard', TemplateView.as_view(template_name = 'user/dashboard.html')),
    path('docs', apiDocs),
    

     
]