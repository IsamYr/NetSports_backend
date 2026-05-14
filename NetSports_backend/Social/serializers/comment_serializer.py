from rest_framework import serializers

from Social.models import Comment

class CommentSerializer(serializers.ModelSerializer):

    usuario_username = serializers.CharField(
        source='usuario.username',
        read_only=True
    )

    fecha_formateada = serializers.SerializerMethodField()


    class Meta:
        model = Comment

        fields = ['id', 'usuario', 'usuario_username', 'contenido', 'texto', 'fecha_formateada']
        read_only_fields = ['usuario', 'fecha']

    def get_fecha_formateada(self, obj):
        return obj.fecha.strftime('%d/%m/%Y %H:%M')