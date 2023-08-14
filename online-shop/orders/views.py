from django.shortcuts import render,redirect
from products.models import Product
from users.models import Profile
from .models import Order,OrderItem
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from .forms import createOrderForm, createOrderItemForm
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
# Create your views here.



####### DO NOT DARE TOUCH THIS FUNCTION########
@login_required(login_url='login')
def getOrders(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    order=Order.objects.get(isPaid=False)

    #get the added product's id
    q= request.GET.get('q') if request.GET.get('q') !=None else ''

    #check if we have a not paid order
    if order:
        #check if product is added as an order item
        if q !='':
            added_product=Product.objects.get(id=q)
            order_item=OrderItem.objects.create(order=order,product=added_product)
        
        orders=order.orderitem_set.all()

    
    else:
        #create an order and then create the order item
        order=Order.objects.create(profile=profile)
        if q !='':
            added_product=Product.objects.get(id=q)
            order_item=OrderItem.objects.create(order=order,product=added_product)
        orders=order.orderitem_set.all()
        
        
           
    #get all order items     
    
    
    #print(f"orderssssssssss:{orders}")
    
    
    if orders is not None:
        total_price=0
        q_product=0
        for o in orders:
            total_price +=o.getPrice
            q_product +=1
        context={'orders':orders,'total_price':total_price,'q_product':q_product}
    else:
        total_price=0
        q_product=0
        context={'orders':orders,'total_price':total_price,'q_product':q_product}
    
        

    #context={'orders':orders,'total_price':total_price,'q_product':q_product}
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




################# Admin functions#######################



#######Order Admin#################
@login_required(login_url='login')
def createOrder(request):
    user=request.user
    
    
    form=createOrderForm()
    form_name='order'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createOrderForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('admin-page')

    context={'form':form,'form_name':form_name}
    return render(request,'orders/form.html',context)


@login_required(login_url='login')
def editOrder(request,pk):
    user=request.user
    order=Order.objects.get(id=pk)
    
    form=createOrderForm(instance=order)
    form_name='edit_order'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createOrderForm(request.POST,instance=order)
            
            if form.is_valid():
                form.save()
                return redirect('admin-page')

    context={'form':form,'form_name':form_name,'order':order}
    return render(request,'orders/form.html',context)

@login_required(login_url='login') 
def deleteOrderAdmin(request,pk):
    user=request.user
    if user.is_staff == True:
        order=Order.objects.get(id=pk)
        order.delete()
       
        return redirect('admin-page')


########### order item Admin###################
@login_required(login_url='login')
def createOrderItem(request):
    user=request.user
    
    form=createOrderItemForm()
    form_name='orderitem'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createOrderItemForm(request.POST)
            
            if form.is_valid():
                form.save()
                
                return redirect('admin-page')

    context={'form':form,'form_name':form_name}
    return render(request,'orders/form.html',context)


@login_required(login_url='login')
def editOrderItem(request,pk):
    user=request.user
    orderitem=OrderItem.objects.get(id=pk)
    
    form=createOrderItemForm(instance=orderitem)
    form_name='edit_orderitem'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createOrderItemForm(request.POST,instance=orderitem)
            
            if form.is_valid():
                form.save()
                return redirect('admin-page')

    context={'form':form,'form_name':form_name,'orderitem':orderitem}
    return render(request,'orders/form.html',context)

@login_required(login_url='login') 
def deleteOrderItemAdmin(request,pk):
    user=request.user
    if user.is_staff == True:
        orderitem=OrderItem.objects.get(id=pk)
        orderitem.delete()
       
        return redirect('admin-page')

