from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from checkin.models import CheckIn
from checkin.serializers import CheckInSerializers, CheckInCreateSerializers
from lokasi.models import Lokasi
from pengguna.models import Pengguna

class CheckinViewSet(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializers
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'head', 'options']
    
    def get_queryset(self):
        return CheckIn.objects.filter(pengguna__user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CheckInCreateSerializers
        return CheckInSerializers

    def create(self, request, *args, **kwargs):
        serializer = CheckInCreateSerializers(data=request.data)
        if serializer.is_valid():
            pengguna, _ = Pengguna.objects.get_or_create(user=self.request.user)
            lokasi = Lokasi.objects.get(qr=serializer.validated_data['lokasi_qr'])
            new_checkin = CheckIn.objects.create(
                pengguna = pengguna,
                lokasi=lokasi
            )
            serializer = CheckInSerializers(new_checkin)
            ret_data = serializer.data
            if pengguna.vaccine_1 and pengguna.vaccine_2:
                ret_data['badge'] = 'green'
            elif pengguna.vaccine_1:
                ret_data['badge'] = 'yellow'
            else:
                ret_data['badge'] = 'red'
                
            return Response(ret_data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            