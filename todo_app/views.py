from django.shortcuts import redirect
from . models import Todo
# Create your views here.
def addTask(request):
    print(request.POST)
    # return redirect('home')
    task = request.POST['new_task']
    Todo.objects.create(task = task)
    return redirect('home')