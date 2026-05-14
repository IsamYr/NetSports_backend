from django.contrib import admin
from Workout.models import Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'repeticiones', 'descripcion', 'dificultad', 'patron_movimiento', 'location')
    list_filter = ('duracion', 'dificultad', 'patron_movimiento', 'location')
    search_fields = ('nombre', 'duracion', 'muscle_group')

admin.site.register(Exercise, ExerciseAdmin)