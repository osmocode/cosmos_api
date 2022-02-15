"""cosmos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from django.contrib import admin
from .views import api_root

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/', api_root),
    path('api/v1/', include('apps.cosmos_auth.urls', namespace='cosmos_auth')),
    path('api/v1/', include('apps.cosmos_users.urls', namespace='cosmos_users')),
]
