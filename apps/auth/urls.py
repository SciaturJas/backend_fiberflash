from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    # path('data-table-clientes/', ClienteViewSet.as_view({'post': 'list_datatable'})),
    ]