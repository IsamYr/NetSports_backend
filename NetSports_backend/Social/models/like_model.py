from django.db import models

class Like(models.Model):
    usuario = models.ForeignKey("Users.Usuario", on_delete=models.CASCADE, verbose_name="Usuario")
    contenido = models.ForeignKey("Social.Content", on_delete=models.CASCADE, verbose_name="Contenido", related_name="likes")

    class Meta:
        unique_together = ("usuario", "contenido")