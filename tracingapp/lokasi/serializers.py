from rest_framework import serializers

from lokasi.models import Lokasi


class LokasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokasi
        fields = ['id', 'qr', 'nama', 'alamat', 'kapasitas'] 
