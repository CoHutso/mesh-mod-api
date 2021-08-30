from django.db.models import fields
from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'email', 'age', 'reg_date')