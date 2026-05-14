from django.contrib import admin
from Workout.models import Routine

class RoutineAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion_total', 'usuario', 'fecha_creacion', 'visibilidad')
    search_fields = ('nombre', 'usuario__username')
    # filter_horizontal = ('visibilidad',)

admin.site.register(Routine, RoutineAdmin)