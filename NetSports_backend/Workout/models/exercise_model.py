from django.db import models

from .exercise_difficulty_model import Difficulty
from .exercise_location_model import Location
from .movement_pattern import MovementPattern
from .muscle_group_model import MuscleGroup

class Exercise(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField(blank=True, null=True, verbose_name="Duración por repetición")
    descripcion = models.TextField(max_length=500, null=True, blank=True, verbose_name="Descripción")
    repeticiones = models.IntegerField(blank=True, null=True, verbose_name="Repeticiones por ronda")
    video = models.URLField(blank=True, null=True, verbose_name="Video")
    miniatura = models.ImageField(blank=True, null=True, verbose_name="Miniatura")
    dificultad = models.CharField(max_length=20, choices=Difficulty.choices, default=Difficulty.BEGINNER, verbose_name="Dificultad")
    patron_movimiento = models.CharField(max_length=20, choices=MovementPattern.choices, default=MovementPattern.PULL, verbose_name="Patron de movimiento")
    location = models.CharField(max_length=20, choices=Location.choices, default=Location.HOME, verbose_name="Entorno")
    muscle_group = models.ManyToManyField(MuscleGroup, related_name="exercises", verbose_name="Grupo muscular")

    def __str__(self):
        return f"Ejercicio: {self.nombre} - Duración aprox: {self.duracion} segundos - Dificultad: {self.dificultad} - Entorno: {self.location} - Patrón de movimiento: {self.patron_movimiento}"