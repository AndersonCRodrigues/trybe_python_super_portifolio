from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from .models import Profile, Project
from .serializer import ProfileSerializer, ProjectSerializer

# Create your views here.


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        return (
            [AllowAny()] if self.action == "retrieve" else [IsAuthenticated()]
        )

    @action(detail=True, methods=["GET"])
    def detailed_info(self, request, pk=None):
        profile = self.get_object()

        context = {
            "profile": profile,
            "projects": profile.projects.all(),
            "certificates": profile.certificates.all(),
        }

        return render(request, "profile_detail.html", context)

    def retrieve(self, request, *args, **kwargs):
        return self.detailed_info(request, *args, **kwargs)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
