from rest_framework.serializers import ModelSerializer
from .models import Certificate, CertifyingInstitution, Profile, Project


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


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class NestedCertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "name"]


class CertifyingInstitutionSerializer(ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ("id", "name", "url", "certificates")

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=certifying_institution,
                **certificate_data,
            )
        return certifying_institution
