from django.contrib import admin
from cicd.models import Repo, GithubToken

admin.site.register(Repo)
admin.site.register(GithubToken)