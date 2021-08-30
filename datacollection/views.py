from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PlayerSerializer
from .models import Player

# Create your views here.
class PlayerViewset(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('name')
    serializer_class = PlayerSerializer