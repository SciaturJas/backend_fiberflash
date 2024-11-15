from django.urls import path, include
from rest_framework import routers

from apps.sales.api.planes_api import AdmPlanesViewSet

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('list-plans/', AdmPlanesViewSet.as_view({'get': 'listar_planes'})),
    ]