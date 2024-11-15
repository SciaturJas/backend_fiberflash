from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.sales.models import Plans
from apps.utils.models import Distritos, Clients


class DistritoFields(serializers.ModelSerializer):
    class Meta:
        model = Distritos
        fields =['id','name']

class ClientFields(serializers.ModelSerializer):
    #distrito / campo de clients
    distrito = DistritoFields(many=False)
    class Meta:
        model = Clients
        fields = '__all__'