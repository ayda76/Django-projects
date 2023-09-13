from django.shortcuts import render, redirect
from .forms import registerUser,updateUserForm
from .models import Profile

from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def loginUser(request):
    page_name='login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username,password=password)

        except:
            messages.error(request,'user does not exist')
            print('username does not exist')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.error(request,'username or password is incorrect')
            print('username or password is incorrect')

    context={'page_name':page_name}
    return render(request,'users/login_register.html',context)

@login_required(login_url='login') 
def logoutUser(request):
    logout(request)
    messages.error(request,'user loged out !!!')
    
    return redirect('login')
    

def register(request):
    page_name='register'
    form=registerUser()
    if request.method == 'POST':
        form=registerUser(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            profile=Profile(
                user=user,
                username=user.username,
                firstname=user.first_name,
                lastname=user.last_name)
            profile.save()
            login(request,user)
            return redirect('home')


        else:
            messages.error(request, 'an error has occurred during registeration')

    context={'page_name':page_name,'form':form}
    return render(request,'users/login_register.html',context)


def update_user(request):
    page_name='update_user'
    user=request.user
    profile=Profile.objects.get(user=user)
    form=updateUserForm(instance=profile)

    if profile:
        if request.method == 'POST':
            form=updateUserForm(request.POST,instance=profile)
            if form.is_valid():
                profile=form.save(commit=False)
                profile.user=user
                profile.save()
                return redirect('home')

            else:
                messages.error(request,'no user found! please login')
                return redirect('login')


    else:
        messages.error(request,'no user found! please login')
        return redirect('login')

    context={'form':form,'page_name':page_name}
    return render(request,'users/login_register.html',context)





                
