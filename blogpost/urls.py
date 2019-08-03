from django.urls import path, include
from . import views


urlpatterns = [
    # path('user/login', ),
    # path('user/register',),
    # path('user/profile'),
    # path('plans/',),
    path('',views.index, name='home'),
]