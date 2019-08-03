from django.contrib import admin
from .models import Plan, LoginData, Profile
# Register your models here.
admin.site.register(Plan)
admin.site.register(LoginData)
admin.site.register(Profile)