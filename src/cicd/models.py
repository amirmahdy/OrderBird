from django.db import models
from django.db.models.constraints import UniqueConstraint


class GithubToken(models.Model):
    name = models.CharField(verbose_name="Name for token", max_length=64)
    token = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.name}"


class Repo(models.Model):
    owner = models.CharField(max_length=128, verbose_name="Owner of repo")
    repository = models.CharField(max_length=128, verbose_name="Repository")
    token = models.ForeignKey(GithubToken, default=None, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["owner", "repository"],
                name="unique_parameter_for_repository",
            )
        ]

    def __str__(self) -> str:
        return f"{self.owner}/{self.repository}"
