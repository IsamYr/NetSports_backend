from django.db import models
import uuid
import os

def user_content_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{extension}"

    return f"content/{instance.usuario.username}/{filename}"

class ContentType(models.TextChoices):
    IMAGE = "image", "Imagen"
    VIDEO = "video", "Video"

class Content(models.Model):
    usuario = models.ForeignKey("Users.Usuario", on_delete=models.CASCADE, related_name="content")
    descripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripcion")
    archivo = models.FileField(upload_to=user_content_path, null=True, blank=True, verbose_name="Archivo")
    tipo_archivo = models.CharField(choices=ContentType.choices, default=ContentType.IMAGE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Usuario: {self.usuario.username}, Archivo: {self.archivo.url}, Fecha publicación: {self.fecha_publicacion}"