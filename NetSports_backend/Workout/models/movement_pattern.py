from django.db import models

class MovementPattern(models.TextChoices):
    PUSH = "push", "Empuje"
    PULL = "pull", "Tirón"
    SQUAT = "squat", "Sentadilla"
    HINGE = "hinge", "Cadera"
    CARRY = "carry", "Carga"