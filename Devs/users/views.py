from django.shortcuts import render,redirect
from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,skills
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProfiles
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def profiles(request):
    profiles,search_query=searchProfiles(request)
    
    context={'profiles':profiles,'search_query':search_query}
    return render(request,'users/profiles.html', context)

def userProfiles(request,pk):
    profile=Profile.objects.get(id=pk)

    topSkills=profile.skills_set.exclude(description__exact="")
    otherSkills=profile.skills_set.filter(description="")
    
    context={'profile':profile, 'topskills':topSkills,'otherskills':otherSkills}
    return render(request, 'users/user-profile.html',context)

def loginUser(request):
    page='login'

    if request.user.is_authenticated:
        return redirect('account')


    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)

        except:
            messages.error(request,'user does not exist')
            print('username does not exist')

        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('account')
        else:
            messages.error(request,'username or password is incorrect')
            print('username or password is incorrect')
    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.error(request,'user loged out !!!')
    return redirect('login')


def registerUser(request):
    page='register'
    form=CustomUserCreationForm()
    if request.method == 'POST':
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            messages.success(request, 'User account was created')
            
            login(request, user)
            return redirect('account')

        else:
            messages.error(request, 'an error has occurred during registeration')



    context={'page':page,'form':form}

    return render(request, 'users/login_register.html',context)



@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    projects= profile.project_set.all()
    skills=profile.skills_set.all()
    

    context={'profile':profile, 'skills':skills, 'projects':projects}
    return render(request,'users/account.html',context)

@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form =ProfileForm(instance=profile)
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES,instance=profile)

        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    return render(request, 'users/profile_form.html',context)


@login_required(login_url='login')
def createSkill(request):
    profile=request.user.profile
    form=SkillForm()
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner=profile
            skill.save()
            messages.success(request, 'skill was added!')
            return redirect('account')


    context={'form':form}
    return render(request,'users/skill_form.html',context)


@login_required(login_url='login')
def updateSkill(request,pk):
    profile=request.user.profile
    skill=profile.skills_set.get(id=pk)

    form=SkillForm(instance=skill)
    if request.method=='POST':
        form=SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'skill was updated!')
            return redirect('account')


    context={'form':form}
    return render(request,'users/skill_form.html',context)

def deleteSkill(request,pk):
    profile=request.user.profile
    skill=profile.skills_set.get(id=pk)
    if request.method=="POST":
        skill.delete()
        messages.success(request, 'skill was deleted!')
        return redirect('account')
    context={'object':skill}
    return render(request,'delete_template.html',context)