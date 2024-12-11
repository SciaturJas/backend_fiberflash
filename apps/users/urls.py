from django.urls import path, include
from rest_framework import routers

from apps.users.api.user_roles import AdmRolesUser

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('list/roles-user/', AdmRolesUser.as_view({'get': 'listar_roles'})),
    ]