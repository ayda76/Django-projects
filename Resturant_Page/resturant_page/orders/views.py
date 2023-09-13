from django.shortcuts import render,redirect
from .models import Order, OrderItem
from users.models import Profile

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def showOrderItems(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    order=Order.objects.get(profile=profile)

    if order is not None:
        orderItems=order.orderitem_set.all()
    else:
        orderItems=[]
        messages.error(request,'username or password is incorrect')

    
    context={'orderItems':orderItems}
    return render(request,'orders/cart.html',context)