from django.urls import path, include
from rest_framework.routers import SimpleRouter

from checkin.views import CheckinViewSet

router = SimpleRouter()
router.register(r'', CheckinViewSet)

urlpatterns = [    
    path('', include(router.urls)),
]
