from django.shortcuts import render, redirect
from .forms import registerUser,updateUserForm, reviewForm
from .models import Profile,Review


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

@login_required(login_url='login')
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



##########################################
##########################################
###############admin######################

def read_Review(request):
    review=Review.objects.all()
    context={'reviews':review}
    return render(request,'users/admin-review-page.html',context)

def update_Review(request,pk):
    page='update_review'
    user=request.user
    review=Review.objects.get(id=pk)
    form=reviewForm(instance=review)
    if user.is_staff:
        if request.method == 'POST':
            form=reviewForm(request.POST,request.FILES,instance=review)
            if form.is_valid():
                form.save()
                return redirect('admin-review-page')
            else:
                pass
    context={'page':page,'form':form,'review':review}
    return render(request,'users/form_page.html',context)

def create_Review(request):
    page='create_review'
    user=request.user
    form=reviewForm()
    if user.is_staff:
        if request.method == 'POST':
            form=reviewForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin-review-page')
            else:
                pass


    context={'page':page,'form':form}
    return render(request,'users/form_page.html',context)

def delete_Review(request,pk):
    review=Review.objects.get(id=pk)
    review.delete()
    
    return redirect('admin-review-page')



def read_User(request):
    users=Profile.objects.all()
    context={'profiles':users}
    return render(request,'users/admin-user-page.html',context)

def update_User(request,pk):
    page='update_user'
    user=Profile.objects.get(id=pk)
    form=updateUserForm(instance=user)
    if request.user.is_staff:
        if request.method == 'POST':
            form=updateUserForm(request.POST,request.FILES,instance=user)
            if form.is_valid():
                form.save()
                return redirect('admin-user-page')
            else:
                pass
    context={'page':page,'form':form,'profile':user}
    return render(request,'users/form_page.html',context)

def create_User(request):
    page='create_user'
    form=registerUser()
    if request.user.is_staff:
        if request.method == 'POST':
            form=registerUser(request.POST,request.FILES)
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
                return redirect('admin-user-page')
            else:
                pass


    context={'page':page,'form':form}
    return render(request,'users/form_page.html',context)

def delete_User(request,pk):
    profile=Profile.objects.get(id=pk)
    profile.user.delete()
    
    profile.delete()
    
    return redirect('admin-user-page')


        
        



            
        

        


                
