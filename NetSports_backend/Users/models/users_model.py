import secrets

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.conf import settings

class UsuarioManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo válido')
        if "@" not in email:
            raise ValueError('No es un formato de correo válido')

        if any(ext in email for ext in settings.EXTENSIONES_BLACKLIST):
            raise ValueError(f"No se puede crear una cuenta con estos formatos: " + ", ".join(settings.EXTENSIONES_BLACKLIST))

        if not password:
            raise ValueError("Contraseña no válida")

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True, blank=False, null=False, verbose_name='Email')
    username = models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name='Nombre de usuario')
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False, verbose_name="Slug")

    is_active = models.BooleanField(default=True, verbose_name="¿Está activo?")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'usuario'
        ordering = ['email']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_hex(16)
            while Usuario.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(16)
            self.slug = prov

        super().save(*args, **kwargs)

    def __str__(self):
        if self.info_personal: # Llamada Clase InfoPersonal (OneToOne con Usuario)
            return f"{self.username}"
        return f"SIN CUENTA"