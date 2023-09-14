from django.shortcuts import render, redirect
from .models import Food 
from users.models import Profile,Review
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def showHome(request):
    foods=Food.objects.all()
    context={'foods':foods}
    return render(request,'foods/home.html', context)

def showMenu(request):
    foods=Food.objects.all()
    context={'foods':foods}
    return render(request,'foods/menu.html', context)

def showFood(request,pk):
    food=Food.objects.get(id=pk)
    
            
    context={'food':food}
    return render(request,'foods/food.html', context)

@login_required(login_url='login')
def createReview(request):
    user=request.user
    profile=Profile.objects.get(user=user)

    if request.method == 'POST':
        comment=request.POST['comment']
        id_food=request.POST['food']
        food=Food.objects.get(id=id_food)

       
        if comment:
            review=Review.objects.create(owner=profile,comment=comment,food=food)
            return redirect('food',food.id)
    