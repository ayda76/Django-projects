from django.shortcuts import render,redirect
from products.models import Product
from users.models import Profile
from .models import Order,OrderItem
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def getOrders(request):
    user=request.user
    q= request.GET.get('q') if request.GET.get('q') !=None else ''
    added_product=Product.objects.get(id=q)
    

    profile=Profile.objects.get(user=user)
    order=profile.order_set.get(isPaid=False)
    
    OrderItem.objects.create(
        order=order,
        product=added_product
    )
    orders=order.orderitem_set.all()

    total_price=0
    q_product=0
    for o in orders:
        total_price +=o.getPrice
        q_product +=1

    context={'orders':orders,'total_price':total_price,'q_product':q_product}
    return render(request,'orders/cart.html',context)


@login_required(login_url='login')
def viewCheckout(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    order=profile.order_set.get(isPaid=False)
    orders=order.orderitem_set.all()

    total_price=0
    q_product=0
    for o in orders:
        total_price +=o.getPrice
        q_product +=1

    context={'profile':profile,'order':order,'orders':orders,'total_price':total_price,'q_product':q_product}
    return render(request,'orders/checkout.html',context)




