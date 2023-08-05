from django.shortcuts import render
from .models import Profile
# Create your views here.

def getUsers(request):

    profiles=Profile.objects.all()

    context={'profiles':profiles}
    return render(request,'users/users.html',context)

def login(request):
    
    return render(request,'users/login.html')


