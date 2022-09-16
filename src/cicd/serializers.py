from rest_framework import serializers
from cicd.models import GithubToken, Repo


class AddTokenSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GithubToken
        fields = (
            "name",
            "token",
        )

class AddRepositorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = (
            "owner",
            "repository",
            "token"
        )

class RepositorySerilizer(serializers.Serializer):
    owner = serializers.CharField(required=True)
    repo = serializers.CharField(required=True)