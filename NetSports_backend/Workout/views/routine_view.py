from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Workout.models import Routine
from Workout.serializers import RoutineSerializer

class RoutineView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        routines = Routine.objects.filter(usuario=request.user).order_by('-fecha_creacion')

        serializer = RoutineSerializer(routines, many=True)

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

class CreateRoutineView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RoutineSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(usuario=request.user)
            return Response({
                "success": True,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DeleteRoutineView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, routine_id):
        routine = Routine.objects.filter(id = routine_id, usuario=request.user).first()

        if not routine:
            return Response({
                "success": False,
                "message": "Rutina no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        routine.delete()

        return Response({
            "success": True,
            "message": "Rutina eliminada de la rutina"
        }, status=status.HTTP_200_OK)
