from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .serializers import ProfileSerializer
from .models import Profile

# Create your views here.
class ProfileRetrieveView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    # lookup_field = "user"
    queryset = Profile.objects.all()
   
