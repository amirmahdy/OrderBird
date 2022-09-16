from django.urls import path
from cicd.views.token import TokenAPIView
from cicd.views.popularity import PopularityAPIView
from cicd.views.repository import RepositoryAPIView

urlpatterns = [
    path("token", TokenAPIView.as_view(), name="token"),
    path("repository", RepositoryAPIView.as_view(), name="repository"),
    path("popularity", PopularityAPIView.as_view(), name="popularity"),
]
