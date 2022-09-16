from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from cicd.serializers import AddRepositorySerilizer
from cicd.models import Repo
from app.exception_handler import unpredicted_exception_handler


class RepositoryAPIView(GenericAPIView):

    @swagger_auto_schema(methods=['post'], request_body=AddRepositorySerilizer)
    @action(detail=False, methods=['post'])
    @unpredicted_exception_handler("DEBUG")
    def post(self, request, *args, **kwargs):
        """
        This method adds Github Repository into system
        input   -- name
        input   -- token
        """
        try:
            serializer = AddRepositorySerilizer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                Repo.objects.create(**data)
                return Response({"message": "OK"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(methods=['get'])
    @action(detail=False, methods=['get'])
    @unpredicted_exception_handler("DEBUG")
    def get(self, request, *args, **kwargs):
        """
        This method returns a list of repository
        output   -- token list
        """
        repositories = Repo.objects.values_list('owner', 'repository').all()
        return Response({"message": repositories}, status=status.HTTP_200_OK)

    @swagger_auto_schema(methods=['patch'], request_body=AddRepositorySerilizer)
    @action(detail=False, methods=['patch'])
    @unpredicted_exception_handler("DEBUG")
    def patch(self, request, *args, **kwargs):
        """
        This method modifies a repository
        """
        serializer = AddRepositorySerilizer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            query_set = Repo.objects.filter(owner=data['owner'], repository=data['repository'])
            if len(query_set) == 0:
                message = "Key not found"
            else:
                message = "Key updated"
                query_set.update(token=data['token'])
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response({"message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
