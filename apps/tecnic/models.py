
from django.db import models

from apps.auth.models import UserProfile
from apps.utils.models import Clients


# Create your models here.

# ESTADOS - PENDIENTE - EN PROCESO - CANCELADO - FINALIZADO
class StatesAverias(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    detail = models.JSONField(default=dict)
    class Meta:
        db_table = 'states_averias'

class Averias(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.JSONField(default=dict)
    date_reporte = models.CharField(max_length=20) #FORMATO TIMESTAMP UNIX
    encargado = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    prioridad = models.CharField(max_length=20)
    state_averia = models.ForeignKey('StatesAverias', on_delete=models.CASCADE)
    date_resolution = models.CharField(max_length=20)
    comentario = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'averias'

