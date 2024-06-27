from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Task

def home(request):
    todos = Task.objects.all()
    return render(request, 'home.html', {'todos': todos})

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status', 'new')
        due_date = request.POST.get('due_date')

        if description and status:
            Task.objects.create(description=description, status=status, due_date=due_date)
        return redirect('home')
    return render(request, 'add.html')
