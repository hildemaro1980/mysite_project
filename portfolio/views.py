from django.shortcuts import render, get_object_or_404
from .models import Project
from blog.models import Post


def home(request):
    projects = Project.objects.all()
    return render(request,"home.html",{"projects":projects})

def test(request):   #just for testing
    my_projects = Project.objects.all()
    #my_projects = Project.objects.order_by('-date')
    #print(my_projects)
    #return render(request,"test.html",{"my_projects":my_projects})
    return render(request,"myhome.html",{"my_projects":my_projects})

def project(request):
    my_projects = Project.object.all()
    return render(request, "myhome.html",{"my_projects":my_projects})

def project_detail(request, project_id):
    print(project_id)    
    project = get_object_or_404(Project, pk = project_id)
    print(project_id)
    return render(request,"project_detail.html",{"project":project})

def startPage(request):
    my_projects = Project.objects.all()
    my_posts = Post.objects.all()
    #my_projects = Project.objects.order_by('-date')
    #return render(request,"test.html",{"my_projects":my_projects})
    return render(request,"startpage.html",{"my_projects":my_projects, "my_posts":my_posts})
