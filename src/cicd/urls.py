from django.urls import path
from cicd.views.add_token import AddTokenAPIView

urlpatterns = [
    path("add_token", AddTokenAPIView.as_view(), name="add_token"),
]