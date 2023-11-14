from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import serializers
from onlineresturant.serializers import OrderSerializer,OrderItemSerializer
from .models import Order,OrderItem
from users.models import Profile
# Create your views here.

@api_view(['GET'])
def getOrders(request):
    orders=Order.object.all()
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addOrder(request):
    data=request.data
    user=request.user
    profile=Profile.objects.get(user=user)
    order=Order.objects.create(
        user=profile
        isPaid=data['isPaid'],
        isDelivered=data['isDelivered']
    )
    serializer=OrderSerializer(order,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    order.delete()

    return Response('Order was deleted')

@api_view(['GET'])
def getOrderItems(request):
    orders=Order.object.all()
    serializer=OrderSerializer(orders,many=True)
    return Response(serializer.data)

