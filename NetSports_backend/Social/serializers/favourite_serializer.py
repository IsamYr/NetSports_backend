from rest_framework import serializers

from Social.models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = '__all__'
        read_only_fields = ['usuario']