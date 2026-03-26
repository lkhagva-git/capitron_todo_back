import logging
import datetime

from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status


from .models import *
from .serializers import *


from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_access(request):
    print("hello")
    return Response(
        {
            "message": "Authenticated access granted",
            "user": request.user.username
        },
        status=status.HTTP_200_OK
    )


# Creates record of user and creates JWT token
@api_view(['POST'])
def signin(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response(
            {"error": "Email and password are required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=email).exists():
        return Response(
            {"error": "User already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=email,   
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "message": "User created successfully",
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        },
        status=status.HTTP_201_CREATED
    )
    

# Retrieves user's data
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_data(request):
    serializer = ProfileSerializer(request.user)
    return Response(serializer.data)


# Creates a task
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        task = serializer.save(user=request.user)
        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieves data of taskes
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# Deletes specific task
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_task(request):
    task_id = request.data.get('id')

    if not task_id:
        return Response({"error": "Task ID is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)


# Updates a task
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_task(request):
    task_id = request.data.get('id')

    if not task_id:
        return Response(
            {"error": "Task ID is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        task = Task.objects.get(id=task_id, user=request.user)
    except Task.DoesNotExist:
        return Response(
            {"error": "Task not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = TaskSerializer(task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












  