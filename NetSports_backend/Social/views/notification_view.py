from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Social.models import Notification
from rest_framework import status

from Social.serializers.notification_serializer import NotificationSerializer


class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        notifications = Notification.objects.filter(destinatario=request.user).order_by('-fecha_creacion')

        serializer = NotificationSerializer(notifications, many=True)

        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class ReadNotificationView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, notification_id):

        notification = Notification.objects.get(id=notification_id, destinatario=request.user)

        notification.leida = True

        notification.save()

        return Response({
            "success": True,
            "message": ("Notification leída -> ", notification.contenido)
        }, status=status.HTTP_200_OK)

class UnreadNotificationCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        count = Notification.objects.filter(destinatario=request.user, leida=False).count()

        return Response({
            "success": True,
            "count": count
        })

class MarkAllNotificationsReadView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        Notification.objects.filter(
            destinatario = request.user,
            leida=False
        ).update(leida=True)

        return Response({
            "success": True,
            "message": "Notificaciones pendientes leídas"
        })