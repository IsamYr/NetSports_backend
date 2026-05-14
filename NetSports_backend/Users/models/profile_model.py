from django.db import models

class Profile(models.Model):
    usuario = models.OneToOneField("Usuario", on_delete=models.CASCADE, related_name="profile") # El perfil depende del usuario
    profile_photo = models.ImageField(upload_to="profile_pics/", default="profile_pics/default_profile.png", verbose_name="Foto de perfil")
    biografia = models.TextField(max_length=500, null=True, blank=True, verbose_name="Biografia")
    visibilidad = models.BooleanField(default=True, verbose_name="Visibilidad")

    class Meta:
        db_table = "profile"
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"Perfil: {self.usuario.username}"