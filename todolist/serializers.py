from rest_framework import serializers
from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ToDoItem
        fields = ['id', 'title', 'description', 'created_by', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']
 