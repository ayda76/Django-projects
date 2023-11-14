from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import serializers
from onlineresturant.serializers import FoodSerializer,CatSerializer,IngredientSerializer
from .models import Food, Cat, Ingredient
# Create your views here.

@api_view(['GET'])
def getFoods(request):
    foods=Food.object.all()
    serializer=FoodSerializer(foods,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addFood(request):
    data=request.data
    food=Food.objects.create(
        name=data['name'],
        cat=data['cat'],
        ingredient=data['ingredient'],
        price=data['price'],
        image=data['image'],
        onMenu=data['onMenu']

    )
    serializer=FoodSerializer(food,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteFood(request,pk):
    food=Food.objects.get(id=pk)
    food.delete()

    return Response('food was deleted')




@api_view(['GET'])
def getCats(request):
    cats=Cat.object.all()
    serializer=CatSerializer(cats,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addCat(request):
    data=request.data
    cat=Cat.objects.create(
        name=data['name']
    )
    serializer=CatSerializer(cat,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCat(request,pk):
    cat=Cat.objects.get(id=pk)
    cat.delete()

    return Response('Cat was deleted')


@api_view(['GET'])
def getIngredients(request):
    ingredients=Ingredient.object.all()
    serializer=IngredientSerializer(ingredients,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addIngredients(request):
    data=request.data
    ingredient=Ingredient.objects.create(
        name=data['name']
    )
    serializer=IngredientSerializer(ingredient,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteIngredient(request,pk):
    ingredient=Ingredient.objects.get(id=pk)
    ingredient.delete()

    return Response('Ingredient was deleted')

