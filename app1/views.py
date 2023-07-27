from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TodoModel
from datetime import datetime
from .permissions import IsOwnerPermission
from .serializer import ToDoSerializer
# Create your views here.
class AllCrateTodoView(generics.ListCreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermission,)
class RUDToDoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (IsOwnerPermission,)

