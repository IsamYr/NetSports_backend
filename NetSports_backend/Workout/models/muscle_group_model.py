from django.db import models

class MuscleGroup(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'