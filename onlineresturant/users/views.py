from django.shortcuts import render
from .models import Profile
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import serializers
from onlineresturant.serializers import ProfileSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self,attrs):
        data=super().validate(attrs)
        serializer=UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k]=v

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    






@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    profiles=Profile.object.all()
    serializer=ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request,pk):

    try:
        profile=Profile.object.get(id=pk)
    except profile.DoesNotExist:
        return Response(serializers.error,status=404)
    serializer=ProfileSerializer(profile,many=False)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(serializers.error,status=400)
    


@api_view(['PUT'])
@permission_classes([IsAdminUser,IsAuthenticated])
def updateUser(request,pk):
    try:
        profile=Profile.object.get(id=pk)
    except profile.DoesNotExist:
        return Response(serializers.error,status=404)

    data=request.data
    profile.user=request.user
    profile.firstname=data['firstname']
    profile.lastname=data['lastname']
    profile.address=data['address']
    profile.tel=data['tel']
    serializer=ProfileSerializer(profile,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializers.error,status=400)

    


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request,pk):
    try:
        profile=Profile.object.get(id=pk)
    except profile.DoesNotExist:
        return Response(serializers.error,status=404)
    profile.delete()

    return Response('profile was deleted')
