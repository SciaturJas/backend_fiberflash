from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager para perfil de usuarios"""

    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Usuario debe tener un email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo base de datos para usuarios en el sistema"""
    email = models.EmailField(max_length=255, unique=True)
    last_login_timetamps_unix = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, unique=True)
    usuario = models.CharField(max_length=20, null=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    detail_user = models.JSONField(null=True)
    objects = UserProfileManager()

    groups = models.ManyToManyField(
        Group,
        related_name='userprofile_set'  # Agrega este related_name único
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='userprofile_permissions_set'  # Nombre único
    )

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name

