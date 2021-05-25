from django.shortcuts import redirect, render
from .models import Todo
from datetime import datetime
# Create your views here.
def Home(request):
    todo=Todo.objects.all()
    return render(request,'index.html',{"todo":todo})

def Add(request):
    if request.method=='POST':
        t=request.POST['task']
        d=request.POST['des']
        Todo.objects.create(task=t,des=d,date=datetime.now())
        return redirect('home')
    return render(request,'add.html')

def Delete(request,pid):
    d=Todo.objects.get(id=pid)
    d.delete()
    return redirect('home')

def Edit(request,pid):
    e=Todo.objects.get(id=pid)
    if request.method=='POST':
        t=request.POST['task']
        d=request.POST['des']
        e.task=t
        e.des=d
        e.save()
        return redirect('home')
    return render(request,'edit.html',{'e':e})
