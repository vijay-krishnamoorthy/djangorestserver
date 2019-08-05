from django.contrib import admin
from .models import Plan, LoginData, ProfileData
# Register your models here.
admin.site.register(Plan)
admin.site.register(LoginData)
admin.site.register(ProfileData)