from rest_framework.viewsets import ModelViewSet
from .models import (
    User,
    Profile,
    Dashboard,
    Recharge,
    Inquiry,
    Dongleplans,
    Prepaidplans,
)
from .serializers import (
    UserSerializer,
    ProfileSerializer,
    RechargeSerializer,
    InquirySerializer,
    PrepaidSerializer,
    DongleSerializer,
)



class UserViewSet(ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=UserSerializer

class ProfileViewSet(ModelViewSet):
    queryset=Dashboard.objects.all()
    serializer_class=ProfileSerializer

# class DashboardViewSet(ModelViewSet):
#     queryset=Dashboard.objects.all()
#     serializer_class=DashboardSerializer

class InquiryViewSet(ModelViewSet):
    queryset=Inquiry.objects.all()
    serializer_class=InquirySerializer

class DongleViewSet(ModelViewSet):
    queryset=Dongleplans.objects.all()
    serializer_class=DongleSerializer

class PrepaidViewSet(ModelViewSet):
    queryset=Prepaidplans.objects.all()
    serializer_class=PrepaidSerializer

class RechargeViewSet(ModelViewSet):
    queryset=Recharge.objects.all()
    serializer_class=RechargeSerializer