from django.shortcuts import render,redirect
from products.models import Product
from users.models import Profile
from .models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def getOrders(request):
    user=request.user
    orders=user.order_set.all()

    total_price=0
    q_product=0
    for order in orders:
        total_price +=order.getPrice
        q_product +=1

    
  

    
    

    context={'orders':orders,'total_price':total_price,'q_product':q_product}
    return render(request,'orders/cart.html',context)


