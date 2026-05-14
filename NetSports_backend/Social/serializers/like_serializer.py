from rest_framework import serializers

from Social.models import Like

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['usuario']