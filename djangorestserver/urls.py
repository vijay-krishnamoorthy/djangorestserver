"""djangorestserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from voizdata import urls
from blogpost import urls
from rest_framework import routers
from voizdata.views import PlanList
from voizdata.viewset import PlanViewSet,LoginViewSet

voizdatarouter = routers.DefaultRouter()
voizdatarouter.register('voizfonica', PlanViewSet)
blogrouter = routers.DefaultRouter()
blogrouter.register('blog',PlanViewSet)
user = routers.DefaultRouter()
user.register('users',LoginViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(voizdatarouter.urls)),
    path('api/', include(user.urls)),
    path('api/voizfonica/', include('voizdata.urls')),
    path('api/blog/', include('voizdata.urls')),
]
