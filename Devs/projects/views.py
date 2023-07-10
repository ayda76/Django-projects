from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects
from django.contrib import messages
# Create your views here.

def projects(request):
    projects,search_query=searchProjects(request)
    
    context={'projects':projects,'search_query':search_query}
    return render(request,'projects/projects.html', context)

def project(request, pk):
    projectObj= Project.objects.get(id=pk)
    tags=projectObj.tags.all()
    form=ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = projectObj
            review.owner = request.user.profile
            review.save()

            projectObj.getVoteCount
            messages.success(request, 'Your review was successfully submitted!')
            return redirect('project', pk=projectObj.id)
        

        

    return render(request,'projects/single_project.html',{'projectObj': projectObj,'tags':tags,'form': form}) 

@login_required(login_url="login")
def createProject(request):
    profile=request.user.profile
    form=ProjectForm()
    if request.method == 'POST':
        newtags=request.POST.get('newtags').replace(','," ",'-').split()
        
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project= form.save(commit=False)
            #we need to asign the project to the profile that created it 
            project.owner=profile
            project.save()
            for tag in newtags:
                tag, created=Tag.objects.get_or_create(name=tag)
                project.tags.add(tag) 
                
            return redirect('projects')
    context={'form':form}
    return render(request,'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)

    if request.method =='POST':
        newtags=request.POST.get('newtags').replace(','," ",'-').split()
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            project=form.save()
            for tag in newtags:
                tag,created=Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            
            return redirect('account')

    context={'form':form}
    return render (request,'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile=request.user.profile
    project= profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
        
    context={'object':project}
    return render(request,'delete_template.html',context)
