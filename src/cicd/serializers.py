from rest_framework import serializers
from cicd.models import GithubToken


class AddTokenSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GithubToken
        fields = (
            "name",
            "token",
        )