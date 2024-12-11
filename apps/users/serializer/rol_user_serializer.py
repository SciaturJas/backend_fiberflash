from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.sales.models import Plans
from apps.users.models import NavBar, UserRol
from apps.utils.models import Distritos, Clients


class NavVarFields(serializers.ModelSerializer):
    class Meta:
        model = NavBar
        fields ='__all__'

class RolesFields(serializers.ModelSerializer):
    rol = NavVarFields(many=False)
    class Meta:
        model = UserRol
        fields ='__all__'