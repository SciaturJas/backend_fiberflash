from django.db import models

# Create your models here.
class Distritos(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    detail = models.JSONField(default=dict)

    class Meta:
        db_table = 'distritos'

class Clients(models.Model):
     name = models.CharField(max_length=100)
     dni = models.CharField(max_length=12)
     address = models.CharField(max_length=100)
     phone = models.CharField(max_length=15)
     usuario = models.CharField(max_length=100)
     password = models.CharField(max_length=100)
     distrito = models.ForeignKey('Distritos', on_delete=models.CASCADE)

     class Meta:
         db_table = 'clients'

class Cajas(models.Model):
    name = models.CharField(max_length=100)
    direction = models.CharField(max_length=300)
    img_eart = models.CharField(max_length=400)
    img_caja = models.CharField(max_length=400)
    detail = models.JSONField(default=dict)
    class Meta:
        db_table = 'cajas'

class StateOnu(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    detail = models.JSONField(default=dict)
    class Meta:
        db_table = 'state_onu'

class Onus(models.Model):
     mac = models.CharField(max_length=100)
     url_image = models.CharField(max_length=400)
     interfaz_user = models.CharField(max_length=100)
     estate_onu = models.ForeignKey('StateOnu', on_delete=models.CASCADE)
     caja = models.ForeignKey('Cajas', on_delete=models.CASCADE, null=True)
     class Meta:
         db_table = 'onus'
