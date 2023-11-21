from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import serializers
from onlineresturant.serializers import FoodSerializer,CatSerializer,IngredientSerializer
from .models import Food, Cat, Ingredient
# Create your views here.

@api_view(['GET'])
def getFoods(request):
    foods=Food.objects.all()
    serializer=FoodSerializer(foods,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFoodById(request,pk):
    try:
        food=Food.objects.get(id=pk)
    except food.DoesNotExist:
        return Response(serializers.error,status=404)
    serializer=FoodSerializer(food,many=False)
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

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateFood(request,pk):
    try:
        food=Food.objects.get(id=pk)
    except food.DoesNotExist:
        return Response(serializers.error,status=404)
    data=request.data
    food.name=data['name']
    food.ingredient = data.get('ingredient')
    food.cat=data['cat']
    food.price= data['price']
    food.image=data['image']
    food.onMenu=data['onMenu']
    serializer=FoodSerializer(food,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializers.error, status=400)



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteFood(request,pk):
    food=Food.objects.get(id=pk)
    food.delete()

    return Response('food was deleted')




@api_view(['GET'])
def getCats(request):
    cats=Cat.objects.all()
    serializer=CatSerializer(cats,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCatById(request,pk):
    try:
        cat=Cat.objects.get(id=pk)
    except cat.DoesNotExist:
        return Response(serializers.error,status=404)
    serializer=CatSerializer(cat,many=False)
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

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateCat(request,pk):
    try:
        cat=Cat.objects.get(id=pk)
    except cat.DoesNotExist:
        return Response(serializers.error, status=404)

    data=request.data
    cat.name=data['name']
    serializer=CatSerializer(cat,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializers.error,status=400)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCat(request,pk):
    cat=Cat.objects.get(id=pk)
    cat.delete()

    return Response('Cat was deleted')


@api_view(['GET'])
def getIngredients(request):
    ingredients=Ingredient.objects.all()
    serializer=IngredientSerializer(ingredients,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getIngredientById(request,pk):
    try:
        ing=Ingredient.objects.get(id=pk)
    except ing.DoesNotExist:
        return Response(serializers.error,status=404)
    serializer=IngredientSerializer(ing,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def addIngredient(request):
    data=request.data
    ingredient=Ingredient.objects.create(
        name=data['name']
    )
    serializer=IngredientSerializer(ingredient,many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateIngredient(request,pk):
    try:
        ing=Ingredient.objects.get(id=pk)

    except ing.DoesNotExist:
        return Response(serializers.error, status=404)

    data=request.data
    ing.name=data['name']
    serializer=IngredientSerializer(ing,many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializers.error, status)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteIngredient(request,pk):
    ingredient=Ingredient.objects.get(id=pk)
    ingredient.delete()

    return Response('Ingredient was deleted')

