from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Social.models import Content, Comment, Notification
from Social.serializers import CommentSerializer


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, content_id):

        content = get_object_or_404(Content, id = content_id)
        comments = content.comments.all().order_by('-fecha')
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, content_id):

        content = get_object_or_404(Content, id = content_id)
        texto = request.data.get('texto', '').strip()

        if not texto or len(texto) == 0:
            return Response({
                "success": False,
                "message": "El comentario no puede estar vacío"
            }, status=status.HTTP_400_BAD_REQUEST)

        if len(texto) > 500:
            return Response({
                "success": False,
                "message": "El comentario no puede ser mayor de 500 caracteres"
            }, status=status.HTTP_400_BAD_REQUEST)

        comment = Comment.objects.create(
            usuario = request.user,
            contenido = content,
            texto = texto
        )

        if content.usuario != request.user:
            Notification.objects.create(
                destinatario = content.usuario,
                emisor = request.user,
                contenido = content,
                tipo = "comment"
            )

        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, content_id, comment_id):

        comment = get_object_or_404(Comment, id=comment_id, content_id=content_id)

        if comment.usuario != request.user and not request.user.is_staff:
            return Response({
                "success": False,
                "message": ("No tienes permiso para eliminar este commentario -> ", comment)
            }, status=status.HTTP_403_FORBIDDEN)

        comment.delete()

        return Response({
            "success": True,
            "message": "Comentario eliminado correctamente"
        }, status=status.HTTP_204_NO_CONTENT)