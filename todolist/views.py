from django.shortcuts import render
from rest_framework import viewsets, permissions
from todolist.permissions import IsOwner
from .models import ToDoItem
from .serializers import ToDoItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return ToDoItem.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        todo_item = self.get_object()
        todo_item.completed = True
        todo_item.save()
        return Response({'status': 'item marked as completed'})
