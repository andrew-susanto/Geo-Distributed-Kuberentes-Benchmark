from django.db import models

from lokasi.models import Lokasi
from pengguna.models import Pengguna

class CheckIn(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.CASCADE)
    lokasi = models.ForeignKey(Lokasi, on_delete=models.CASCADE)
    crowd = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.id == None:
            loc_crowd = CheckIn.objects.filter(lokasi=self.lokasi, active=True).count()
            self.crowd = loc_crowd
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.created_at.strftime("%d %B %Y %H:%M:%S.%f")