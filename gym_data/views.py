# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SliderHome
from .serializers import TodoSerializer,UserSerializer,CreateUserSerializer
from rest_framework.parsers import JSONParser

from rest_framework import viewsets, permissions, generics
from knox.models import AuthToken
from django.contrib.auth import authenticate


class TodoListApiView(APIView):

    def get(self, request, *args, **kwargs):
        todos = SliderHome.objects.filter()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request, *args, **kwargs):
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TodoSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return Response(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationAPI(generics.GenericAPIView):

    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(generics.GenericAPIView):

    serializer_class = CreateUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = authenticate(serializer)





