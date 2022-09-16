from django.urls import path
from cicd.views.add_token import AddTokenAPIView
from cicd.views.popularity import PopularityAPIView

urlpatterns = [
    path("add_token", AddTokenAPIView.as_view(), name="add_token"),
    path("popularity", PopularityAPIView.as_view(), name="popularity"),
]