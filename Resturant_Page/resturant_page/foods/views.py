from django.shortcuts import render, redirect
from .models import Food 
# Create your views here.

def showHome(request):
    foods=Food.objects.all()
    context={'foods':foods}
    return render(request,'foods/home.html', context)

def showMenu(request):
    foods=Food.objects.all()
    context={'foods':foods}
    return render(request,'foods/menu.html', context)
