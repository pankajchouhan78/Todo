from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from . models import Todo
# Create your views here.


def addTask(request):
    # print(request.POST)
    task = request.POST['new_task']
    Todo.objects.create(task = task)
    return redirect('home')

def mark_as_done(request,pk):
    # return HttpResponse(pk)
    task = get_object_or_404(Todo, pk=pk)
    # print(task)
    task.is_completed = True
    task.save()
    return redirect('home')
    
def mark_as_undone(request,pk):
    task = get_object_or_404(Todo, pk=pk)
    print(task)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    update_task = get_object_or_404(Todo,pk=pk)
    if request.method =="POST":
        new_task = request.POST['new_task']
        update_task.task = new_task
        update_task.save()
        return redirect('home')
    else:
        context = {
            'task':update_task,
        }
        return render(request,"edit_task.html",context)
    
def delete_task(request,pk):
    task = get_object_or_404(Todo,pk=pk)
    task.delete()
    return redirect('home')