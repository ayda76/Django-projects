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
    order=Order.objects.get(profile=profile)

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
    order=profile.order_set.filter(isPaid=False)

    if order is not None:
        orderItem=OrderItem.objects.create(
            order=order,
            food_item=food_item)
        orderItem.save()
        order.save()
        return redirect('orders')       
    
    else:
        order=Order.objects.create(profile=profile)
            
        orderItem=OrderItem.objects.create(
            order=order,
            food_item=food_item)    
                
        orderItem.save()
        order.save()
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
    qty=request.POST['qty']

    
    if int(qty) != orderItem.qty & qty is not None:
        orderItem.qty=int(qty)
        orderItem.save()
        return redirect('orders')

    return redirect('orders')

@login_required(login_url='login')
def makeOrder(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    order=profile.order_set.filter(isPaid=False)
    
    context={'order':order,'profile':profile}

    if order is not None:
        if profile.address is not None:
            orderItems=order.orderitem_set.all()  
            
            context={'orderItems':orderItems,'profile':profile}
            
        else:
            return redirect('update_user')

    
        
    return render(request,'orders/paybill.html',context)

        
        



            
        

        


        


    
