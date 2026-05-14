from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Users.models import Profile

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username=None):

        if username:
            print("Hay username -> ", username)

            profile = Profile.objects.filter(usuario__username=username).first()
            print("Entonces el perfil sería este -> ", profile)

            if not profile:
                return Response(
                    {"success": False, "message": "Perfil no encontrado"},
                    status=status.HTTP_404_NOT_FOUND
                )

            profile_data = {
                "username": profile.usuario.username,
                "profile_photo": profile.profile_photo.url,
                "visibilidad": profile.visibilidad,
            }

            if profile.visibilidad or profile.usuario == request.user:
                info = getattr(profile.usuario, "info_personal", None)

                if info:
                    profile_data.update({
                        "altura_cm": info.altura_cm,
                        "peso_kg": info.peso_kg,
                        "fecha_union": str(info.fecha_union),
                        "nombre": info.nombre,
                        "apellidos": info.apellidos,
                        "telefono": info.telefono,
                        "fecha_nacimiento": str(info.fecha_nacimiento),
                    })

                profile_data.update({
                    "biografia": profile.biografia,
                })

            return Response({"data": profile_data, "success": True}, status=status.HTTP_200_OK)

        profiles = Profile.objects.exclude(usuario=request.user)

        data = []
        for profile in profiles:
            data.append({
                "username": profile.usuario.username,
                "profile_photo": profile.profile_photo.url,
                "visibilidad": profile.visibilidad,
            })

        return Response({"data": data, "success": True}, status=status.HTTP_200_OK)

class MyProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.filter(usuario=request.user).first()

        if not profile:
            return Response({"success": False, "message": "Perfil no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            "id": profile.id,
            "username": profile.usuario.username,
            "profile_photo": profile.profile_photo.url,
            "biografia": profile.biografia,
            "visibilidad": profile.visibilidad,
        }

        return Response({"data": data, "success": True}, status=status.HTTP_200_OK)

class UpdateMyProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        try:
            profile = Profile.objects.get(usuario=request.user)
        except Profile.DoesNotExist:
            return Response({"success": False, "message": "Perfil no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        if 'biografia' in request.data:
            profile.biografia = request.data.get('biografia')

        if 'visibilidad' in request.data:
            visibilidad = request.data.get('visibilidad')
            if isinstance(visibilidad, str):
                profile.visibilidad = visibilidad.lower() in ['true', '1', 'yes']
            else:
                profile.visibilidad = bool(visibilidad)

        if 'profile_photo' in request.FILES:
            # print('Foto recibida: ', request.FILES.get('profile_photo'))
            profile.profile_photo = request.FILES.get('profile_photo')

        profile.save()

        return Response({
            "success": True,
            "message": "Perfil actualizado",
            "data": {
                "biografia": profile.biografia,
                "visibilidad": profile.visibilidad,
                "profile_photo": profile.profile_photo.url,
            }
        }, status=status.HTTP_200_OK)

