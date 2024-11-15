from django.urls import path, include
from rest_framework import routers

from apps.utils.api.clients_api import AdmClientViewSet

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('list/all-clients/', AdmClientViewSet.as_view({'get': 'listar_clientes'})),
    ]