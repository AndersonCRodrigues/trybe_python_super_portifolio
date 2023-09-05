# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProfileSerializer
from .models import Profile

# Create your views here.


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
