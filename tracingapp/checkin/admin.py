from django.contrib import admin
from checkin.models import CheckIn

@admin.register(CheckIn)
class Admin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    