from django.db import models
from django.contrib.auth.models import User

class Pengguna(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nik = models.CharField(max_length=16, null=True, blank=True)
    vaccine_1 = models.BooleanField(default=False)
    vaccine_2 = models.BooleanField(default=False)
    
    class Meta:
        indexes = [
            models.Index(fields=['user'])
        ]
    
    def __str__(self) -> str:
        return f"{self.user}"