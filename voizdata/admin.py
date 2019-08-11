from django.contrib import admin
from .models import (
    Plan,
    User,
    ProfileData,
    Recharge,
    NewConnection
)
# Register your models here.
admin.site.register(Plan)
admin.site.register(User)
admin.site.register(ProfileData)
admin.site.register(NewConnection)
admin.site.register(Recharge)
# admin.site.register(NewConnection)
# admin.site.register(NewConnection)
# admin.site.register(NewConnection)
