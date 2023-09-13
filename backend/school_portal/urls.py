"""school_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_auth.urls')),
    path('', include('account.urls')),
    
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name = 'password_reset.html'),
        name='password_reset'

    ),
    path(
        'pasword-reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name= 'password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_complete'
    ),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


]

# urlpatterns += urlpatterns = [
#     ...
#     path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
# ]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.MEDIA_ROOT)
