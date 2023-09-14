from django.shortcuts import render,redirect
from .models import Order, OrderItem
from foods.models import Food
from users.models import Profile

from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def showOrderItems(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    orders=Order.objects.filter(profile=profile)
    order=None
    #order=profile.order_set.filter(isPaid=False)
    for i in orders:
        if i.isPaid == False:
            order=i
        else:
            pass

    if order is not None:
        orderItems=order.orderitem_set.all()
    else:
        orderItems=[]
        messages.error(request,'username or password is incorrect')

    
    context={'orderItems':orderItems}
    return render(request,'orders/cart.html',context)

@login_required(login_url='login')
def createOrders(request,pk):
    food_item=Food.objects.get(id=pk)
    user=request.user
    profile=Profile.objects.get(user=user)
    #order=Order.objects.filter(profile=profile).filter(isPaid=False) 
    orders=Order.objects.filter(profile=profile)
    order=None
    #order=profile.order_set.filter(isPaid=False)
    for i in orders:
        if i.isPaid == False:
            order=i
        else:
            pass
    print(f"orderrrrrrrr:{order}")

    if order:
        orderItem=OrderItem.objects.create(
            order=order,
            food_item=food_item)
        
        return redirect('orders')  
           
        
    
    else:
        order=Order.objects.create(profile=profile)
            
        orderItem=OrderItem.objects.create(order=order,food_item=food_item)    
                
        
        return redirect('orders') 
        


    orderItems=order.orderitem_set.all()  
    context={'orderItems':orderItems} 
    return render(request,'orders/cart.html',context)       

@login_required(login_url='login')
def deleteOrderItem(request,pk):
    orderItem=OrderItem.objects.get(id=pk)
    orderItem.delete()
    return redirect('orders')   

@login_required(login_url='login')
def updateOrderItem(request,pk):
    orderItem=OrderItem.objects.get(id=pk)
    if request.method == 'POST':
        qty=request.POST['qty']
    else:
        qty=1
    

    
    if qty != orderItem.qty:

        if qty is not None:
            orderItem.qty=qty
            orderItem.save()
            return redirect('orders')
        

    return redirect('orders')

@login_required(login_url='login')
def makeOrder(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    orders=Order.objects.filter(profile=profile)
    order=None
    #order=profile.order_set.filter(isPaid=False)
    for i in orders:
        if i.isPaid == False:
            order=i
        else:
            pass
    context={'profile':profile}

    if order is not None:
        
        if profile.address is not None:
            
            orderItems=order.orderitem_set.all()  
            total_price=0
            for item in orderItems:
                total_price+=item.getPrice
            context={'order':order,'profile':profile,'total_price':total_price}
            
        else:
            return redirect('update_user')
        
    return render(request,'orders/paybill.html',context)
@login_required(login_url='login')
def paybill(request,pk):
    order=Order.objects.get(id=pk)
    
    if order is not None:
        order.isPaid=True
        order.save()
        context={'order':order}
        return render(request,'orders/factor.html',context)


   

        
        



            
        

        


        


    
