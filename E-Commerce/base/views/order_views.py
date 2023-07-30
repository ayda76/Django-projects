from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import JsonResponse
from base.models import Product , Order , OrderItem
from django.contrib.auth.models import User
from base.serializers import ProductSerializer, OrderSerializer


from django.contrib.auth.hashers import make_password
from rest_framework import status


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItems(request):
    user=request.user
    data=request.data
    orderItems =data['orderItems']
    if orderItems and len(orderItems) == 0:
        return Response({'detail':'no order items'}, status=status.HTTP_400_BAD_REQUEST)

    else:
        #create order -> create shipping address -> create order items ->update stock
        order=Order.objects.create(
            user=user,
            paymentMethod=data['paymentMethod'],
            taxPrice=data['taxPrice'],
            shippingPrice=data['shippingPrice'],
            totalPrice=data['totalPrice']
        )

        shipping=shippingaddress.objects.create(
            order=order,
            address=data['shippingAddress']['address'],
            city=data['shippingAddress']['city'],
            postalcode=data['shippingAddress']['postalcode'],
            country=data['shippingAddress']['country'],
        )

        for i in orderItems:
            product =Product.objects.get(_id=i['product'])
            item =OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                qty=i['qty'],
                price=i['price'],
                image=product.image.url,
            )

            product.countInStock -= item.qty
            product.save()

    serializer=OrderSerializer(order,many=True)

    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderById(request,pk):

    user=request.user

    try:
        order=Order.objects.get(_id=pk)
        if user.is_staff or order.user == user:
            
            serializer =OrderSerializer(order,many=False)
            return Response(serializer.data)

        else:
            return Response({'detail':'not authorized to view this order'}, status=status.HTTP_400_BAD_REQUEST)


    except:
        return Response({'detail':'order does not exist'}, status=status.HTTP_400_BAD_REQUEST) 
        


    