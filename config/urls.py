"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.http import JsonResponse
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshSlidingView,
    TokenVerifyView,
)

def main_view(request):
    return JsonResponse({'message': 'server on'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='/'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/admin/', include('apps.admin.urls')),
    path('api/auth/', include('apps.auth.urls')),
    path('api/cobranza/', include('apps.cobranza.urls')),
    path('api/sales/', include('apps.sales.urls')),
    path('api/tecnic/', include('apps.tecnic.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/utils/', include('apps.utils.urls')),
]
