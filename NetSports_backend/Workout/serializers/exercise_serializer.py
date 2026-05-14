from rest_framework import serializers

from Workout.models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):

    muscle_group = serializers.StringRelatedField(many=True)
    dificultad_display = serializers.CharField(
        source='get_dificultad_display',
        read_only=True
    )
    location_display = serializers.CharField(
        source='get_location_display',
        read_only=True
    )
    patron_movimiento_display = serializers.CharField(
        source='get_patron_movimiento_display',
        read_only=True
    )

    class Meta:
        model = Exercise
        fields = '__all__'