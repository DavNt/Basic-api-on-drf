from rest_framework import viewsets
from .serializers import PictureSerializer, PicIdSerializer
from .models import Picture, PicId


class PictureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class PicIdViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PicId.objects.all()
    serializer_class = PicIdSerializer