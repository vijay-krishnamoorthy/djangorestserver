from .models import Plan,Profile,LoginData
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields= '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginData
        fields = '__all__'