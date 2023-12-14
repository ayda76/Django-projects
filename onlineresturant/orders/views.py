from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import serializers
from onlineresturant.serializers import OrderReadSerializer,OrderWriteSerializer,OrderItemReadSerializer,OrderItemWriteSerializer
from foods.models import Food
from .models import Order,OrderItem
from users.models import Profile
# Create your views here.

@api_view(['GET'])
def getOrders(request):
    orders=Order.objects.all()
    serializer=OrderReadSerializer(orders,many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getOrderById(request,pk):
    try:
        order=Order.objects.get(id=pk)
    except order.DoesNotExist:
        return Response(serializers.error,status=404)
    serializer=OrderReadSerializer(order,many=False)
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
        serializer=OrderWriteSerializer(data=request.data,many=False)
        if serializer.is_valid():
            serializer.save()
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
    serializer=OrderWriteSerializer(order,data=data,many=False)
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
    serializer=OrderItemReadSerializer(orderItems,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getOrderItem(request,pk):
    orderItem=OrderItem.objects.get(id=pk)
    serializer=OrderItemReadSerializer(orderItem,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addOrderItem(request):
    user=request.user
    data=request.data
    serializer=OrderItemWriteSerializer(data=request.data,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.data)
    


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateOrderItemQTY(request,pk):
    try:
        orderItem=OrderItem.objects.get(id=pk)
    except orderItem.DoesNotExist:
        return Response(serializers.error,status=404)
    data=request.data
    
  
    serializer=OrderItemWriteSerializer(orderItem,data=data,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializers.error,status=400)



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteOrderItem(request,pk):
    orderitem=OrderItem.objects.get(id=pk)
    orderitem.delete()

    return Response('OrderItem was deleted')