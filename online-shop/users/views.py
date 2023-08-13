from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.models import User
from .forms import registerUserProfileForm , updateProfileForm
from django.contrib.auth.decorators import login_required
from .utils import  getProfilesPage,deleteProfilePage,editProfilePage
from orders.models import Order,OrderItem
from products.models import Product,Review,Tag,Color,Size,Category

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


@login_required(login_url='login') 
def logoutUser(request):
    logout(request)
    messages.error(request,'user loged out !!!')
    
    return redirect('login')



@login_required(login_url='login') 
def updateProfile(request):
    
    user=request.user
    profile=Profile.objects.get(user=user)
    form=updateProfileForm(instance=profile)

    if request.method =='POST':
        form=updateProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            print('saved the form')
            return redirect('checkout')

        else:
            messages.error(request,'no user found! please login')
        
    
    context={'form':form}
    return  render(request,'users/user_info_confirmation.html',context)

    

@login_required(login_url='login') 
def getAdminPages(request):
    user=request.user
    q= request.GET.get('q') if request.GET.get('q') !=None else ''
    if user.is_staff==True :
        page_name='profiles'
        context={'page_name':page_name}
        if q == '' or q == 'profiles':
            page_name='profiles'
            profiles=Profile.objects.all()
            context={'profiles':profiles,'page_name':page_name}
            
        elif q == 'cat':
            page_name='cat'
            cats=Category.objects.all()
            context={'cats':cats,'page_name':page_name}
            
            
        elif q == 'size':
            page_name='size'
            sizes=Size.objects.all()
            context={'sizes':sizes,'page_name':page_name}
            
            
        elif q == 'color':
            page_name='color'
            colors=Color.objects.all()
            context={'colors':colors,'page_name':page_name}
        elif q == 'tag':
            page_name='tag'
            tags=Tag.objects.all()
            context={'tags':tags,'page_name':page_name}
        elif q == 'product':
            page_name='product'
            products=Product.objects.all()
            context={'products':products,'page_name':page_name}
        elif q == 'review':
            page_name='review'
            reviews=Review.objects.all()
            context={'reviews':reviews,'page_name':page_name}
        elif q == 'order':
            page_name='order'
            order=Order.objects.all()
            context={'order':order,'page_name':page_name}
        else:
            page_name='orderitem'
            orderitems=OrderItem.objects.all()
            context={'orderitems':orderitems,'page_name':page_name}

        return render(request,'users/adminpanel.html',context)

        






 
