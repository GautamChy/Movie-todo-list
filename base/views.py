from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todolist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodolistSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'index.html')
    

def contact_us(request):
    return HttpResponse('This is contact function')

def about_us(request):
    return HttpResponse('This is about_us function')

def home(request):
    person =[
        
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 14},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 40},
    {"name": "Ethan", "age": 60}
]
                  
    
    
            
    context = {       # dictionary form ko laagi context hunchha
        "name":"Home page",
        "age": 25,
        "persons":person
    }
    return render (request,'home.html',context) # render means display 

def list(request):
    obj = todolist.objects
    task = obj.all()
    all = obj.all().count()
    completed = obj.filter(is_completed = True).count()
    not_completed = obj.filter(is_completed = False).count()
    
    context = {
        "tasks" : task,
        "alll" : all,
        "completedd" :completed,
        "not_completedd" :not_completed
        
    }
    
    return render (request,'task.html',context)

def create (request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title == '' and description == '':
            context = {
                "error" : "Both fields are required."
                 }
            return render(request,'create.html',context)
        
        todolist.objects.create(title = title, description = description) # Right side ko title todolist maa vaako and left side ko title user ley post garey ko title 
        return redirect('/task')
    
    return render(request,'create.html')

def mark(request, pk):
    task = todolist.objects.get(pk = pk)
    task.is_completed = True
    task.save()
    return redirect('/task')
    

def edit(request,pk):
    task = todolist.objects.get(pk = pk)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('/task')
    context = {
        "task" : task
    }
    return render(request,'edit.html',context)

def delete(request, pk):
    task = todolist.objects.filter(pk=pk)
    task.delete()
    return redirect('/task')  


@api_view(['GET','POST'])
def todo_list(request):
    if request.method == 'GET':
        todolist_objects = todolist.objects.all()
        serializer = TodolistSerializer(todolist_objects,many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodolistSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({
            "Details": "New todolist created"
        }, status=status.HTTP_201_CREATED)
   
@api_view(['GET','DELETE','PUT','PATCH'])        
def todo_list_detail(request,id):
    if request.method == 'GET':
        todolist_objects = get_object_or_404 (todolist,id = id)
        serializer = TodolistSerializer(todolist_objects)
        return Response(serializer.data) 
    
    elif request.method == 'DELETE':
            todolist_objects = todolist.objects.get(id = id)
            todolist_objects.delete()
            return Response({
                'Details':"Todolist item has been successfully deleted"
            },status=status.HTTP_204_NO_CONTENT)
        
        
    elif request.method == 'PUT':
        todolist_objects = todolist.objects.get(id=id)
        serializer = TodolistSerializer(todolist_objects,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Details":"Todolist item has been successfully updated with the provided details"
        },status=status.HTTP_202_ACCEPTED)
        
        
    elif request.method == 'PATCH':
        todolist_objects = todolist.objects.get(id=id)
        serializer = TodolistSerializer(todolist_objects,data = request.data,partial = True)
        serializer.is_valid()
        serializer.save()
        return Response({
            "Details":"Todolist item has been partially updated with the provided details"
        },status=status.HTTP_206_PARTIAL_CONTENT)
       
            
        
    
        
        
        
        
            
         
    

    





    