from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from checkin.models import CheckIn

class CheckInSerializers(ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['pengguna', 'lokasi', 'crowd', 'created_at', 'active']
        depth = 1
        
class CheckInCreateSerializers(Serializer):
    lokasi_qr = serializers.CharField(max_length=32)
