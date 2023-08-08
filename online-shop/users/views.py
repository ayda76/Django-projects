from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.models import User
from .forms import registerUserProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def getUsers(request):

    profiles=Profile.objects.all()

    context={'profiles':profiles}
    return render(request,'users/users.html',context)

def loginUser(request):
    page_name='login'

    if request.user.is_authenticated:
        return redirect('products')

    if request.method == 'POST':
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
            return redirect('products')
        else:
            messages.error(request,'username or password is incorrect')
            print('username or password is incorrect')
    
    context={'page_name':page_name}
    return render(request, 'users/login_register.html',context)

def registerUser(request):
    form=registerUserProfileForm()
    page_name='register'

    if request.method == 'POST':
        form=registerUserProfileForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            user=form.save()
            messages.success(request, 'User account was created')
            
            login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'an error has occurred during registeration')

    context={'page_name':page_name,'form':form}

    

    return render(request,'users/login_register.html',context)


    



 