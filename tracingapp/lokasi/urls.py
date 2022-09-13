from django.urls import path, include
from rest_framework.routers import SimpleRouter

from lokasi.views import LokasiViewSet

router = SimpleRouter()
router.register(r'', LokasiViewSet)

urlpatterns = [    
    path('', include(router.urls)),
]
