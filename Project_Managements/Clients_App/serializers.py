from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  # Or 'first_name', 'last_name' if you want to include more details

class ClientSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)  # This will show the user's details instead of the ID

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
