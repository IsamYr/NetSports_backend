from rest_framework import serializers

from Social.models import Content, Like, Favourite
from Social.serializers import CommentSerializer


class ContentSerializer(serializers.ModelSerializer):

    usuario_username = serializers.CharField(
        source="usuario.username",
        read_only=True
    )

    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    favourites_count = serializers.SerializerMethodField()
    user_liked = serializers.SerializerMethodField()
    user_favourited = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = ['id', 'usuario', 'usuario_username', 'descripcion', 'archivo', 'tipo_archivo', 'fecha_publicacion', 'fecha_actualizacion', 'likes_count', 'comments_count', 'favourites_count', 'user_liked', 'user_favourited', 'comments']
        read_only_fields = ['usuario', 'fecha_publicacion']

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_favourites_count(self, obj):
        return obj.favourites.count()

    def get_user_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Like.objects.filter(usuario=request.user, contenido=obj).exists()
        return False

    def get_user_favourited(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Favourite.objects.filter(usuario=request.user, contenido=obj).exists()
        return False

