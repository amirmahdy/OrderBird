from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from cicd.serializers import AddRepositorySerilizer
from cicd.models import Repo


class RepositoryAPIView(GenericAPIView):

    @swagger_auto_schema(methods=['post'], request_body=AddRepositorySerilizer)
    @action(detail=False, methods=['post'])
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
    def get(self, request, *args, **kwargs):
        """
        This method returns a list of repository
        output   -- token list       
        """
        repositories = Repo.objects.values_list('owner', 'repository').all()
        return Response({"message": repositories}, status=status.HTTP_200_OK)