from django.db import models

from apps.auth.models import UserProfile


# Create your models here.

class NavBar(models.Model):

    is_rol = models.CharField(max_length=20)
    detail = models.JSONField(null=True)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'nav_bar'


class UserRol(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rol = models.ForeignKey('NavBar', on_delete=models.CASCADE)
    state = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'user_rol'