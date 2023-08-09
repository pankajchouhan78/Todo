from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import Todo

def home(request):
    task = Todo.objects.filter(is_completed = False).order_by('-updated_at')
    completed_task = Todo.objects.filter(is_completed = True)
    # print(completed_task)
    context = {
        'task':task,
        'completed_task':completed_task,
    }
    return render(request,"home.html",context)