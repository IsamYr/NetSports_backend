from django.db import models

class Difficulty(models.TextChoices):
    BEGINNER = "begginer", "Principiante"
    INTERMEDIATE = "intermediate", "Intermedio"
    ADVANCED = "advanced", "Avanzado"