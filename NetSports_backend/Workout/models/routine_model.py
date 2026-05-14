from django.db import models
from Workout.models.exercise_model import Exercise

class Routine(models.Model):
    usuario = models.ForeignKey("Users.Usuario", on_delete=models.CASCADE, related_name="routine")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripcion de la rutina")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    ejercicios = models.ManyToManyField(Exercise, related_name="rutinas", blank=True, verbose_name="Ejercicios")
    visibilidad = models.BooleanField(default=False, verbose_name="Visibilidad")

    @property
    def duracion_total(self):
        return sum(
            ejercicio.duracion or 0
            for ejercicio in self.ejercicios.all()
        )

    def __str__(self):
        return f"Rutina: {self.nombre} - Duracion total: {self.duracion_total}"