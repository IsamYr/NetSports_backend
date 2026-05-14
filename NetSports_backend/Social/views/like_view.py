from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Social.models import Content, Like, Notification


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, content_id):

        content = get_object_or_404(Content, id = content_id)
        likes_count = content.likes.count()
        user_liked = False

        if request.user.is_authenticated:
            user_liked = Like.objects.filter(
                usuario = request.user,
                contenido = content
            ).exists()

        return Response({
            "likes_count": likes_count,
            "user_liked": user_liked
        }, status=status.HTTP_200_OK)

    def post(self, request, content_id):

        content = get_object_or_404(Content, id = content_id)
        usuario = request.user

        like, created = Like.objects.get_or_create(usuario=usuario, contenido=content)

        if content.usuario != request.user:
            Notification.objects.create(
                destinatario=content.usuario,
                emisor=request.user,
                contenido=content,
                tipo="like"
            )

        if not created:
            like.delete()
            return Response({
                "message": "Like quitado",
                "liked": False
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Like agregado",
            "liked": True
        }, status=status.HTTP_201_CREATED)
