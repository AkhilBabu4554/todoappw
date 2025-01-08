from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Task,User
from .forms import UsercreateForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def task_view(request):
    Tasks=Task.objects.filter(User=request.user).order_by('Completed','Title')
    return render(request,"Home.html",{'Tasks':Tasks})



def create_view(request): 
    if request.method=='POST':
        taskname=request.POST.get('taskname')
        if taskname:
            newtask=Task(Title=taskname,User=request.user)
            newtask.save()
            return redirect("TaskList")
    else:
        return render(request,"new_task.html")
    

        
    
def update_view(request,id):
    task=get_object_or_404(Task,pk=id,User=request.user)
    if request.method=='POST':
        newtitle =request.POST.get('taskname')
        if newtitle:
            task.Title=newtitle
            task.save()
        return redirect("TaskList")
    return render(request,"update_task.html",{"task":task})

def deleteview(request,id):
    task=get_object_or_404(Task,pk=id,User=request.user)
    task.delete()
    return redirect("TaskList")

def Toggleview(request,id):
    task=get_object_or_404(Task,pk=id,User=request.user)
    task.Completed=not task.Completed

    task.save()
    return redirect("TaskList")



# authentication

def RegisterView(request):
    if request.method=="POST":
        form= UsercreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UsercreateForm()
    return render(request,'Register.html',{'form':form})
    

def loginview(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('TaskList')
        else:
            pass    
    else:
        pass
    return render(request,'login.html')
    
def logoutview(request):
    logout(request)
    return redirect('TaskList')