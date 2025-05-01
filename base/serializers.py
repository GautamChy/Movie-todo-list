from rest_framework import serializers
from .models import todolist

class TodolistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField()
    description = serializers.CharField()
    is_completed = serializers.BooleanField()
    
    def create(self,validated_data):
        return todolist.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_completed = validated_data.get('is_completed', instance.is_completed)
        instance.save()
        return instance