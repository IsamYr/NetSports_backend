from django.db import models

class InfoPersonal(models.Model):
    usuario = models.OneToOneField("Usuario", on_delete=models.CASCADE, related_name="info_personal")
    nombre = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre')
    apellidos = models.CharField(max_length=100, blank=False, null=False, verbose_name='Apellidos')
    telefono = models.CharField(max_length=11, blank=False, null=False, verbose_name="Telefono")
    fecha_nacimiento = models.DateField(blank=False, null=False, verbose_name="Fecha de nacimiento")
    altura_cm = models.FloatField(blank=True, null=True, verbose_name="Altura en cm")
    peso_kg = models.FloatField(blank=True, null=True, verbose_name="Peso en kg")
    fecha_union = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de union")

    class Meta:
        db_table = 'information_personal'
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
        ordering = ['id', 'fecha_union']

    def __str__(self):
        return f"Nombre: {self.nombre}, Telefono: {self.telefono}"