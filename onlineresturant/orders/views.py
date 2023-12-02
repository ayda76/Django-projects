from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import serializers
from onlineresturant.serializers import OrderSerializer,OrderItemSerializer
from foods.models import Food
from .models import Order,OrderItem
from users.models import Profile
# Create your views here.

@api_view(['GET'])
def getOrders(request):
    orders=Order.objects.all()
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getOrderById(request,pk):
    try:
        order=Order.objects.get(id=pk)
    except order.DoesNotExist:
        return Response(serializers.error,status=404)
    serializer=OrderSerializer(order,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addOrder(request):
    data=request.data
    user=request.user
    orders=Order.objects.all()
    check=False
    for item in orders:
        if item.isPaid==False:
            check=True
    
    if check==False:
        profile=Profile.objects.get(user=user)
        order=Order.objects.create(
            user=profile,
            isPaid=data['isPaid'],
            isDelivered=data['isDelivered'])

        serializer=OrderSerializer(order,many=False)
        return Response(serializer.data)
    else:
        return Response('An unpaid order exists still!!!!')


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrder(request,pk):
    try:
        order=Order.objects.get(id=pk)
    except order.DoesNotExist:
        return Response(serializers.error,status=404)
    data=request.data
    serializer=OrderSerializer(order,data=data,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializers.error,status=400)



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    order.delete()

    return Response('Order was deleted')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllOrderItems(request):
    orderItems=OrderItem.objects.all()
    serializer=OrderItemSerializer(orderItems,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderItem(request,pk):
    orderItem=OrderItem.objects.get(id=pk)
    serializer=OrderItemSerializer(orderItem,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItem(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    order=None

    try:
        order=profile.order_set.get(isPaid=False)
    except Order.DoesNotExist:
        pass
    if order is None:
        order=Order.objects.create(user=profile,isPaid=False,isDelivered=False)

        
    data=request.data
    food_item=data['food']

    food=Food.objects.get(id=food_item['id'])
    orderItem=OrderItem.objects.create(
        order=order,
        food=food,
        user=profile,
        qty=data['qty']
    )
    serializer=OrderItemSerializer(orderItem,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializers.error,status=400)
    


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderItemQTY(request,pk):
    try:
        orderItem=OrderItem.objects.get(id=pk)
    except orderItem.DoesNotExist:
        return Response(serializers.error,status=404)
    data=request.data
    
    orderItem.qty=data['qty']
    serializer=OrderItemSerializer(orderItem,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializers.error,status=400)



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteOrderItem(request,pk):
    orderitem=OrderItem.objects.get(id=pk)
    ordeitemr.delete()

    return Response('OrderItem was deleted')