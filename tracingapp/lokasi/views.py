from django.db.models.base import Model
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser

from lokasi.models import Lokasi
from lokasi.serializers import LokasiSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class LokasiViewSet(ModelViewSet):
    queryset = Lokasi.objects.all()
    serializer_class = LokasiSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    lookup_field = 'qr'
