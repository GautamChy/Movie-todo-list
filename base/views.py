from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todolist


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
    task = todolist.objects.get(pk=pk)
    task.delete()
    return redirect('/task')    # or your task list URL



    