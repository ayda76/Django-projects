from django.shortcuts import render,redirect
from products.models import Product
from users.models import Profile
from .models import Order,OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def getOrders(request):
    orders=Order.objects.all()

    context={'orders':orders}
    return render(request,'orders/cart.html',context)



@login_required(login_url='login')
def makeOrder(request,pk):

    user=request.user
    profile=Profile.objects.get(user=user)
    product=Product.objects.get(id=pk)
    order=Order.objects.create(
        profile=profile

    )

    orderItem=OrderItem.objects.create(
        order=order,
        product=product
    )

    return render(request,'orders/cart.html')



    
    
