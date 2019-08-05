from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import (
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView
    )
from .models import Plan, LoginData, ProfileData
from .serializer import PlanSerializer
# Create your views here.
def index(request):
    return render(request,'index.html')

class PlanList(ListAPIView):
    queryset= Plan.objects.all()
    serializer_class = PlanSerializer
    template_name='index.html'

class PlanDetailsView(RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    template_name='plan_detail_view.html'

class PlanDestroyView(DestroyAPIView):
    queryset=Plan.objects.all()
    serializer_class = PlanSerializer
    template_name= 'plan_destroy_view.html'

class PlanUpdateView(UpdateAPIView):
    queryset=Plan.objects.all()
    serializer_class =PlanSerializer
    template_name='plan_update_view.html'

class PlanCreateView(CreateAPIView):
    queryset=Plan.objects.all()
    serializer_class=PlanSerializer
    template_name='plan_create_view.html'