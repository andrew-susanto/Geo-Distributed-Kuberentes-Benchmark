from django.shortcuts import render
from django.http import JsonResponse

def healthcheck(request):
    return JsonResponse({"status": "OK"})