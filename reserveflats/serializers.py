# serializers.py
from rest_framework import serializers

from .models import ReserveFlats

class ReserveFlatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReserveFlats
        fields = ('id', 'floor', 'price', 'reserved')