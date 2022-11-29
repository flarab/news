from rest_framework import viewsets

from . import serializers
from apps.news.models import New


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = serializers.NewsSerializer
