from django.db import models

class Comment(models.Model):
    usuario = models.ForeignKey("Users.Usuario", on_delete=models.CASCADE, verbose_name="Usuario")
    contenido = models.ForeignKey("Social.Content", on_delete=models.CASCADE, verbose_name="Contenido", related_name="comments")
    texto = models.TextField(max_length=500, verbose_name="Texto")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")