from django.db import models

from apps.utils.models import Clients


# Create your models here.

class Plans(models.Model):
    name = models.CharField(max_length=100)
    cantidad_mb = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    detail = models.JSONField(default=dict)
    class Meta:
        db_table = 'plans'

class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.JSONField(default=dict)
    class Meta:
        db_table = 'services'

class StateSales(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    detail = models.JSONField(default=dict)
    class Meta:
        db_table = 'state_sales'

class Sales(models.Model):
    cliente = models.ForeignKey(Clients, on_delete=models.CASCADE)
    service = models.ForeignKey('Services', on_delete=models.CASCADE)
    plan = models.ForeignKey('Plans', on_delete=models.CASCADE)
    estate_sales = models.ForeignKey('StateSales', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        db_table = 'sales'
