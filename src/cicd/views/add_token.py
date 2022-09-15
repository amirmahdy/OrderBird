from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from drf_yasg import openapi
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from datetime import datetime
from cicd.serializers import AddTokenSerilizer 
name = openapi.Parameter('name', openapi.IN_QUERY, description="Name for Token", type=openapi.TYPE_STRING)
token = openapi.Parameter('token', openapi.IN_QUERY, description="Token Value", type=openapi.TYPE_STRING)


class AddTokenAPIView(GenericAPIView):

    @swagger_auto_schema(methods=['get'], manual_parameters=[name, token])
    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        """
        input   -- name
        input   -- token        
        """
        serializer = AddTokenSerilizer(data=request.GET)
        if serializer.is_valid():
            data = serializer.validated_data
            return Response({"message": data}, status=status.HTTP_200_OK)
        else:
            return Response({"message": str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)