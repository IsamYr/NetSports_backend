from django.db import models

class Location(models.TextChoices):
    HOME = "home", "Casa"
    GYM = "gym", "Gimnasio"
    OUTDOOR = "outdoor", "Exterior"