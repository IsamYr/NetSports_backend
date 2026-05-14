from django.contrib import admin
from Workout.models import MuscleGroup

class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(MuscleGroup, MuscleGroupAdmin)