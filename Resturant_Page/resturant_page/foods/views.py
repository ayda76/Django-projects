from django.shortcuts import render, redirect
from .models import Food ,Ingredient
from users.models import Profile,Review
from .forms import FoodForm,IngredientForm
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
    

#########################################################
#########################################################
############ admin ######################################
@login_required(login_url='login')
def read_Food(request):
    foods=Food.objects.all()
    context={'foods':foods}
    return render(request,'foods/admin_page.html',context)

@login_required(login_url='login')
def update_Food(request,pk):
    page='update'
    user=request.user
    food=Food.objects.get(id=pk)
    form=FoodForm(instance=food)
    if user.is_staff:
        if request.method == 'POST':
            form=FoodForm(request.POST,request.FILES,instance=food)
            if form.is_valid():
                form.save()
                return redirect('admin-page')
            else:
                pass
    context={'page':page,'form':form,'food':food }
    return render(request,'foods/form_page.html',context)

@login_required(login_url='login')
def create_Food(request):
    page='create'
    user=request.user
    form=FoodForm()
    if user.is_staff:
        if request.method == 'POST':
            form=FoodForm(request.POST,request.FILES)
            if form.is_valid:
                form.save()
                return redirect('admin-page')
            else:
                pass


    context={'page':page,'form':form}
    return render(request,'foods/form_page.html',context)

@login_required(login_url='login')
def delete_Food(request,pk):
    food=Food.objects.get(id=pk)
    food.delete()
    
    return redirect('admin-page')

@login_required(login_url='login')
def read_Ingredient(request):
    ingredients=Ingredient.objects.all()
    context={'ingredients':ingredients}
    return render(request,'foods/admin_ingredient_page.html',context)

@login_required(login_url='login')
def update_Ingredient(request,pk):
    page='update_ingredient'
    user=request.user
    ingredient=Ingredient.objects.get(id=pk)
    form=IngredientForm(instance=ingredient)
    if user.is_staff:
        if request.method == 'POST':
            form=IngredientForm(request.POST,request.FILES,instance=ingredient)
            if form.is_valid():
                form.save()
                return redirect('admin-ingredient-page')
            else:
                pass
    context={'page':page,'form':form,'ingredient':ingredient}
    return render(request,'foods/form_page.html',context)

@login_required(login_url='login')
def create_Ingredient(request):
    page='create_ingredient'
    user=request.user
    form=IngredientForm()
    if user.is_staff:
        if request.method == 'POST':
            form=IngredientForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('admin-ingredient-page')
            else:
                pass


    context={'page':page,'form':form}
    return render(request,'foods/form_page.html',context)
@login_required(login_url='login')
def delete_Ingredient(request,pk):
    ingredient=Ingredient.objects.get(id=pk)
    ingredient.delete()
    
    return redirect('admin-ingredient-page')

