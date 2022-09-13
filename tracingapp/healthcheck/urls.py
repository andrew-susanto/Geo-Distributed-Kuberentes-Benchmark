from django.urls import path

from healthcheck import views

urlpatterns = [
    path('', views.healthcheck),
]