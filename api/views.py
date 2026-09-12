from django.shortcuts import render
from .serializers import(
     TaskSerializers,
     RegisterSerializer,
     LoginSerializer
)
from  rest_framework import generics
from task.models import Task
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate,login


class TaskDetail(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   

class TaskView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    lookup_field = 'pk'


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Registration successful"},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )




class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return Response(
                    {"message": "Login successful"},
                    status=status.HTTP_200_OK
                )

            return Response(
                {"message": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )