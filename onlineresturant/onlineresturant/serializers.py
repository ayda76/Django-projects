from rest_framework import serializers
from foods.models import Food,Cat,Ingredient
from users.models import Profile
from orders.models import Order,OrderItem

class CatSerializer(serializers.ModelSerializer):
    food=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cat
        fields = '__all__'

    def get_food(self,obj):
        items=obj.food_set.all()
        serializer=FoodSerializer(items,many=True)

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    cat= CatSerializer(many=False)
    ingredient=IngredientSerializer(many=True)
    class Meta:
        model = Food
        fields = '__all__'

    



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    orderitems=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
    def get_orderitem(self,obj):
        items=obj.orderitem_set.all()
        serializer=OrderItemSerializer(items,many=True)

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'