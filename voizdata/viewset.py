from rest_framework import viewsets
from .models import Plan
from .models import User, ProfileData
from .serializer import PlanSerializer, UserSerializer, ProfileSerializer
from django.views.decorators.csrf import csrf_exempt



class PlanViewSet(viewsets.ModelViewSet):
    queryset= Plan.objects.all()
    serializer_class = PlanSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

	# def list(self, request):
 #        queryset = User.objects.all()
 #        serializer = UserSerializer(queryset, many=True)
 #        return Response(serializer.data)

 #    def retrieve(self, request, pk=None):
 #        queryset = User.objects.all()
 #        user = get_object_or_404(queryset, pk=pk)
 #        serializer = UserSerializer(user)
 #        return Response(serializer.data)

class ProfileViewSet(viewsets.ModelViewSet):
	queryset = ProfileData.objects.all()
	serializer_class = ProfileSerializer