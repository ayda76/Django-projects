from django.shortcuts import render,redirect
from products.models import Product
from users.models import Profile
from .models import Order,OrderItem
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def getOrders(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    order=profile.order_set.get(isPaid=False)
    #get the added product's id
    q= request.GET.get('q') if request.GET.get('q') !=None else ''

    #check if we have a not paid order
    if order:
        #check if product is added as an order item
        if q !='':
            added_product=Product.objects.get(id=q)
            OrderItem.objects.create(order=order,product=added_product)
            

    else:
        #create an order and then create the order item
        order=Order.objects.create(profile=profile)
        if q !='':
            added_product=Product.objects.get(id=q)
            OrderItem.objects.create(order=order,product=added_product)
           
    #get all order items     
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


@login_required(login_url='login')
def deleteOrderItem(request,pk):
    order_item=OrderItem.objects.get(id=pk)
    order_item.delete()

    return redirect('orders')

@login_required(login_url='login')
def updateOrder(request,pk):
    qty= request.GET.get('qty') if request.GET.get('qty') !=None else ''
    if qty != '':
        order_item=OrderItem.objects.get(id=pk)
        if order_item.qty != qty:
            order_item.qty= qty
            order_item.save()

            return redirect('orders')

        else:
            pass

    return redirect('orders')

@login_required(login_url='login')
def submitOrder(request,pk):
    user=request.user
    profile=Profile.objects.get(user=user)
    order=profile.order_set.get(id=pk,isPaid=False)
    orders=order.orderitem_set.all()

    total_price=0
    q_product=0
    for o in orders:
        total_price +=o.getPrice
        q_product +=1
        
    if order:
        order.isPaid=True
        order.paidAt= datetime.now()
        order.save()
    else:
        messages.error(request,'order does not exist!')
    


    context={'profile':profile,'order':order,'orders':orders,'total_price':total_price,'q_product':q_product}
    return render(request,'orders/factor.html',context)

