from rest_framework import serializers
from .models import Picture, PicId


class PictureSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Picture
        fields = ['id', 'author', 'width', 'height', 'url', 'download_url']


class PicIdSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = PicId
        fields = ['id', 'url']
