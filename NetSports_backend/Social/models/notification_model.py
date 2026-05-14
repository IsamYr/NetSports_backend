from django.db import models

class Notification(models.Model):
    LIKE = "like"
    COMMENT = "comment"
    FAVOURITE = "favourite"

    TYPE_CHOICES = [
        (LIKE, "Like"),
        (COMMENT, "Comentario"),
        (FAVOURITE, "Favorito")
    ]

    destinatario = models.ForeignKey("Users.Usuario", on_delete=models.CASCADE, related_name="notifications")
    emisor = models.ForeignKey("Users.Usuario", on_delete=models.CASCADE, null=True, blank=True)
    contenido = models.ForeignKey('Social.Content', on_delete=models.CASCADE, null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TYPE_CHOICES)
    leida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Notificacion'
        verbose_name_plural = 'Notificaciones'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.emisor.username} -> {self.tipo}"