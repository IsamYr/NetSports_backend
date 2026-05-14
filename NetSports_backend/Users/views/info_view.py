from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import InfoPersonal


class MyInfoPersonalView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        info = InfoPersonal.objects.filter(usuario=request.user).first()

        data = {
            "username": info.usuario.username,
            "nombre": info.nombre,
            "apellidos": info.apellidos,
            "telefono": info.telefono,
            "fecha_nacimiento": info.fecha_nacimiento,
            "altura_cm": info.altura_cm or 0,
            "peso_kg": info.peso_kg or 0,
            "fecha_union": str(info.fecha_union),
        }

        return Response({"data": data, "success": True}, status=status.HTTP_200_OK)

    def patch(self, request):
        info = InfoPersonal.objects.filter(usuario=request.user).first()

        allowed_fields = ['nombre', 'apellidos', 'telefono', 'altura_cm', 'peso_kg']

        for field in allowed_fields:
            if field in request.data:
                setattr(info, field, request.data[field])

        info.save()

        return Response({"success": True, "message": "Información actualizada"})

class UpdateMyInfoPersonalView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        try:
            info_personal = InfoPersonal.objects.get(usuario=request.user)
        except InfoPersonal.DoesNotExist:
            return Response({
                "success": False,
                "message": "Inf"
            })

        if 'nombre' in request.data:
            info_personal.nombre = request.data.get('nombre')

        if 'apellidos' in request.data:
            info_personal.apellidos = request.data.get('apellidos')

        if 'telefono' in request.data:
            info_personal.telefono = request.data.get('telefono')

        if 'fecha_nacimiento' in request.data:
            info_personal.fecha_nacimiento = request.data.get('fecha_nacimiento')

        if 'altura_cm' in request.data:
            info_personal.altura_cm = request.data.get('altura_cm')

        if 'peso_kg' in request.data:
            info_personal.peso_kg = request.data.get('peso_kg')

        info_personal.save()

        return Response({
            "success": True,
            "message": "Información personal actualizada",
            "data": {
                "nombre": info_personal.nombre,
                "apellidos": info_personal.apellidos,
                "telefono": info_personal.telefono,
                "fecha_nacimiento": str(info_personal.fecha_nacimiento),
                "altura_cm": info_personal.altura_cm or 0,
                "peso_kg": info_personal.peso_kg or 0,
            }
        }, status=status.HTTP_200_OK)

