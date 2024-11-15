import decimal
from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.http import JsonResponse

import json
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.sales.models import Plans
from apps.sales.serializer import planes_serializer


class AdmPlanesViewSet(viewsets.ViewSet):
    # permission_classes = [IsAuthenticated]


    @action(detail=False, methods=['get'])
    def listar_planes(self, request):

        # planes = list(Plans.objects.all().values())

        planes = Plans.objects.all()
        plans_serializer = planes_serializer.PlansFields(planes, many=True).data
        return JsonResponse({'success': True, 'messaje': '', 'data': plans_serializer},
                            status=status.HTTP_200_OK)
