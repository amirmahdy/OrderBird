from rest_framework import serializers
from cicd.models import GithubToken


class AddTokenSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GithubToken
        fields = (
            "name",
            "token",
        )

class RepositorySerilizer(serializers.Serializer):
    owner = serializers.CharField(required=True)
    repo = serializers.CharField(required=True)