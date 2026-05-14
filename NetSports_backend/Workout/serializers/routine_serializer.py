from rest_framework import serializers

from Workout.models import Routine
from Workout.serializers import ExerciseSerializer

class RoutineSerializer(serializers.ModelSerializer):

    ejercicios = ExerciseSerializer(many=True, read_only=True)

    duracion_total = serializers.SerializerMethodField()

    class Meta:
        model = Routine
        fields = [
            'id',
            'nombre',
            'descripcion',
            'fecha_creacion',
            'visibilidad',
            'duracion_total',
            'ejercicios',
        ]

        read_only_fields = [
            'usuario',
            'fecha_creacion'
        ]

    def get_duracion_total(self, obj):
        total = 0
        for exercise in obj.ejercicios.all():
            total += exercise.duracion * exercise.repeticiones
        return total