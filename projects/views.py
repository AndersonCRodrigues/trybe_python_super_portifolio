# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProfileSerializer, ProjectSerializer
from .models import Profile, Project

# Create your views here.


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
