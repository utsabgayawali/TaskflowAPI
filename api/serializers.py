from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate





class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def create(self, validated_data):

        user = User.objects.create_user(
        username=validated_data['username'],
        password=validated_data['password']
        )

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
