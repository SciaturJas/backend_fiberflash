from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.http import JsonResponse

import json
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.sales.models import Plans
from apps.sales.serializer import planes_serializer
from apps.utils.models import Clients
from apps.utils.serializer import cliente_serializer


class AdmClientViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def listar_clientes(self, request):

        clientes = Clients.objects.all()
        client_serializer = cliente_serializer.ClientFields(clientes, many=True).data
        return JsonResponse({'success': True, 'messaje': '', 'data': client_serializer},
                            status=status.HTTP_200_OK)
