from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from apps.sales.models import Plans


class PlansFields(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ['id','name']