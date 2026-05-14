from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Social.models import Content, Favourite, Notification
from Social.serializers import ContentSerializer


class FavouriteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, content_id):

        content = get_object_or_404(Content, id=content_id)
        is_favourite = False

        if request.user.is_authenticated:
            is_favourite = Favourite.objects.filter(
                usuario=request.user,
                contenido=content
            ).exists()

        return Response({
            "is_favourite": is_favourite
        }, status=status.HTTP_200_OK)

    def post(self, request, content_id):

        content = get_object_or_404(Content, id=content_id)
        usuario = request.user

        favourite, created = Favourite.objects.get_or_create(
            usuario=usuario,
            contenido=content
        )

        if not created:
            favourite.delete()
            return Response({
                "success": True,
                "message": "Removido de favoritos",
                "is_favourite": False
            }, status=status.HTTP_200_OK)

        if content.usuario != request.user:
            Notification.objects.create(
                destinatario = content.usuario,
                emisor = request.user,
                contenido = content,
                tipo = "favourite"
            )

        return Response({
            "success": True,
            "message": "Añadido a favoritos",
            "is_favourite": True
        }, status=status.HTTP_201_CREATED)

    def get_user_favourites(self, request):

        favourites = Favourite.objects.filter(usuario=request.user).select_related("contenido")
        contents = [fav.contenido for fav in favourites]
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)