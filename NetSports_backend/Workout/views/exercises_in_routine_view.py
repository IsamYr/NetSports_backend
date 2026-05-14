from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Workout.models import Routine, Exercise

class AddExerciseToRoutineView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, routine_id):

        exercise_id = request.data.get("exercise_id")

        if not exercise_id:
            return Response({
                "success": False,
                "message": "Debes enviar un ejercicio"
            }, status=status.HTTP_400_BAD_REQUEST)

        routine = Routine.objects.filter(
            id = routine_id,
            usuario = request.user
        ).first()

        if not routine:
            return Response({
                "success": False,
                "message": "Rutina no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        exercise = Exercise.objects.filter(id = exercise_id).first()

        if not exercise:
            return Response({
                "success": False,
                "message": "Ejercicio no encontrado"
            }, status=status.HTTP_404_NOT_FOUND)

        routine.ejercicios.add(exercise)

        return Response({
            "success": True,
            "message": "Ejercicio añadido a la rutina"
        }, status=status.HTTP_200_OK)

class RemoveExerciseFromRoutineView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, routine_id):
        exercise_id = request.data.get("exercise_id")

        if not exercise_id:
            return Response({
                "success": False,
                "message": "Debes enviar un ejercicio"
            }, status=status.HTTP_400_BAD_REQUEST)

        routine = Routine.objects.filter(id = routine_id, usuario=request.user).first()

        if not routine:
            return Response({
                "success": False,
                "message": "Rutina no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        exercise = Exercise.objects.filter(id = exercise_id).first()

        if not exercise:
            return Response({
                "success": False,
                "message": "Ejercicio no encontrado"
            }, status=status.HTTP_404_NOT_FOUND)

        routine.ejercicios.remove(exercise)

        return Response({
            "success": True,
            "message": "Ejercicio eliminado de la rutina"
        }, status=status.HTTP_200_OK)