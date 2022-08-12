from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView


class LoginAPI(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response({
            'request': request.data 
        }, status=status.HTTP_200_OK)
