from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from Workout.models import Exercise
from Workout.serializers import ExerciseSerializer

class ExerciseView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        exercises = Exercise.objects.all()

        serializer = ExerciseSerializer(
            exercises,
            many=True,
        )

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)