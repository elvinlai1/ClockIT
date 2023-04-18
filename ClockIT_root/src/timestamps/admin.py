from django.contrib import admin
from .models import Timestamps, TimestampsLog

# Register your models here.

admin.site.register(Timestamps)
admin.site.register(TimestampsLog)