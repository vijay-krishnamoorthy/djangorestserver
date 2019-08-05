from .models import Plan,ProfileData,LoginData
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields= '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileData
        fields = '__all__'