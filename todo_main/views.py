from django.shortcuts import render
from django.http import HttpResponse
from todo_app.models import Todo

def home(request):
    task = Todo.objects.filter(is_completed = False).order_by('-updated_at')
    context = {
        'task':task,
    }
    return render(request,"home.html",context)