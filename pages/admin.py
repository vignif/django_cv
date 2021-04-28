from django.contrib import admin

# Register your models here.
from .models import UserInfo, WorkExperience

admin.site.register(UserInfo)
admin.site.register(WorkExperience)