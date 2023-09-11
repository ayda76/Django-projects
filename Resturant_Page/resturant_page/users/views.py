from django.shortcuts import render
from .forms import registerUser
# Create your views here.
def login(request):

    
    return render(request,'users/login_register.html')

def register(request):
    return render(request,'users/login_register.html')