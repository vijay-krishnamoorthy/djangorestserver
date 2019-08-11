from .models import Plan,ProfileData,User
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields= '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileData
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        lookup_field='username'