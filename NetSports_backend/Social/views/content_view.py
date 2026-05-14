from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Social.models import Content
from Social.serializers import ContentSerializer


class ContentView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        contents = Content.objects.all().order_by('-fecha_actualizacion', '-fecha_publicacion')

        serializer = ContentSerializer(contents, many=True)

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = ContentSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(usuario=request.user)

            return Response({
                "success": True,
                "data": serializer.data
            })

        return Response({
            "success": False,
            "message": ("Error al publicar el contenido: ", serializer.errors)
        }, status=status.HTTP_400_BAD_REQUEST)

class MyContentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, content_id):

        content = Content.objects.get(id = content_id, usuario=request.user)

        serializer = ContentSerializer(content)

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, content_id):

        try:
            content = Content.objects.get(id=content_id,usuario=request.user)
        except Content.DoesNotExist:
            return Response({
                "success": False,
                "message": "Publicación no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ContentSerializer(content, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()
            return Response({
                "success": True,
                "data": serializer.data
            })

        return Response({
            "success": False,
            "message": ("Error al publicar el contenido: ", serializer.errors)
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, content_id):

        try:
            content = Content.objects.get(id=content_id,usuario=request.user)
        except Content.DoesNotExist:
            return Response({
                "success": False,
                "message": "Publicación no encontrada"
            }, status=status.HTTP_404_NOT_FOUND)

        content.delete()

        return Response({
            "success": True,
            "message": "Publicación eliminado"
        }, status=status.HTTP_200_OK)

class MyContentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = Content.objects.filter(usuario=request.user).order_by('-fecha_publicacion')

        serializer = ContentSerializer(content, many=True)

        return Response({
            "success": True,
            "data": serializer.data
        }, status=status.HTTP_200_OK)
