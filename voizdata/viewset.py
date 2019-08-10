from rest_framework import viewsets
from .models import Plan
from .models import LoginData
from .serializer import PlanSerializer, LoginSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset= Plan.objects.all()
    serializer_class = PlanSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset=LoginData.objects.all()
    serializer_class = LoginSerializer