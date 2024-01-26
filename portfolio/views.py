from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request,"home.html",{"projects":projects})

def test(request):
    my_projects = Project.objects.all()
    #my_projects = Project.objects.order_by('-date')
    print(my_projects)
    #return render(request,"test.html",{"my_projects":my_projects})
    return render(request,"myhome.html",{"my_projects":my_projects})

def startPage(request):
    my_projects = Project.objects.all()
    #my_projects = Project.objects.order_by('-date')
    print(my_projects)
    #return render(request,"test.html",{"my_projects":my_projects})
    return render(request,"startpage.html",{"my_projects":my_projects})
