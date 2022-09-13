from django.db import models
import uuid

class Lokasi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    qr = models.CharField(max_length=32, unique=True)
    nama = models.CharField(max_length=64)
    alamat = models.CharField(max_length=256)
    kapasitas = models.IntegerField()
    
    class Meta:
        indexes = [
            models.Index(fields=['qr'])
        ]
        
    def __str__(self) -> str:
        return self.nama
    
    
