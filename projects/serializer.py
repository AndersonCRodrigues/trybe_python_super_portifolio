from rest_framework.serializers import ModelSerializer
from .models import Profile, Project


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "name", "github", "linkedin", "bio")


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        )
