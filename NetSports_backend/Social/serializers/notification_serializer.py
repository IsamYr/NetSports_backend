from rest_framework import serializers
from Social.models import Notification

class NotificationSerializer(serializers.ModelSerializer):

    emisor_username = serializers.CharField(source='emisor.username', read_only=True)

    # comentario_emisor = serializers.CharField

    contenido_id = serializers.IntegerField(source='contenido.id', read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'tipo', 'leida', 'fecha_creacion', 'emisor_username', 'contenido_id']


    # def get_comentario_emisor(self, obj):
    #     return Notification.objects.get(id=1)