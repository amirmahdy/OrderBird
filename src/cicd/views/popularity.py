from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from drf_yasg import openapi
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from cicd.serializers import RepositorySerilizer
from cicd.github import GithubRepoClass

owner = openapi.Parameter('owner', openapi.IN_QUERY, description="Owner", type=openapi.TYPE_STRING)
repo = openapi.Parameter('repo', openapi.IN_QUERY, description="Repo", type=openapi.TYPE_STRING)


class PopularityAPIView(GenericAPIView):

    @swagger_auto_schema(methods=['get'], manual_parameters=[owner, repo])
    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        """
        This method adds Github token into system
        input   -- name
        input   -- token        
        """
        serializer = RepositorySerilizer(data=request.GET)
        if serializer.is_valid():
            data = serializer.validated_data
            github = GithubRepoClass(**data)
            result = github.call_api()
            return Response({"message": "OK"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
