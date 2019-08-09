from django.contrib import admin
from .models import (
    Plan,
    LoginData,
    ProfileData,
    Recharge,
    NewConnection
) 
# Register your models here.
admin.site.register(Plan)
admin.site.register(LoginData)
admin.site.register(ProfileData)
admin.site.register(NewConnection)
admin.site.register(Recharge1)
#admin.site.register(NewConnection)
#admin.site.register(NewConnection)
#admin.site.register(NewConnection)
