
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.auth import decode_token
from apps.auth.models import UserProfile
from apps.users.models import UserRol
from apps.users.serializer import rol_user_serializer


class AdmRolesUser(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def listar_roles(self, request):
        key = request.META.get('HTTP_AUTHORIZATION').split()[1]
        patrocinador_id = decode_token.execute(key)
        user = UserProfile.objects.filter(id=int(patrocinador_id)).first()

        roles = UserRol.objects.filter(user_id=user.id).all()
        rol_ser = rol_user_serializer.RolesFields(roles, many=True).data
        return JsonResponse({'success': True, 'cantidad': None, 'data': rol_ser},
                            status=status.HTTP_200_OK)