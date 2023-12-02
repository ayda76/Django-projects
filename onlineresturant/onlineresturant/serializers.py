from rest_framework import serializers
from foods.models import Food,Cat,Ingredient
from users.models import Profile
from orders.models import Order,OrderItem

class CatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cat
        fields = '__all__'

    def update(self,instance, validatedData):
        instance.name=validatedData.get('name', instance.name)
        instance.save()
        return instance


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


    def update(self,instance, validatedData):
        instance.name=validatedData.get('name',instance.name)
        instance.save()
        return instance



class FoodSerializer(serializers.ModelSerializer):
    cat= CatSerializer(many=False)
    ingredient=IngredientSerializer(many=True)
    class Meta:
        model = Food
        fields = '__all__'
    
    def get_ingredient(self,obj):
        items=obj.ingredient.all()
        serializer=IngredientSerializer(items,many=True)
        return serializer.data

    def update(self, instance,validatedData):
        instance.name = validatedData.get('name', instance.name)
        instance.price = validatedData.get('price', instance.price)
        instance.onMenu = validatedData.get('onMenu', instance.onMenu)
        # Update the related fields
        # Extract the 'ingredient' data from the validated data, defaulting to an empty list
        ingredient_data = validatedData.pop('ingredient',[])
       
        for ing in ingredient_data:
            # The **ingredient_item unpacks the dictionary into keyword arguments for the get_or_create method
            ingredient_obj, created = Ingredient.objects.get_or_create(**ing)
            instance.ingredient.add(ingredient_obj)

        
        cat_data = validatedData.pop('cat', {})
        cat_obj, created = Cat.objects.get_or_create(**cat_data)
        instance.cat = cat_obj
         
        instance.save()
        return instance




    



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    orderitems=serializers.SerializerMethodField(read_only=True)
    user=ProfileSerializer(many=False)
    class Meta:
        model = Order
        fields = '__all__'
    def get_orderitems(self,obj):
        items=obj.orderitem_set.all()
        serializer=OrderItemSerializer(items,many=True)
        return serializer.data

    def update(self,instance, validatedData):
        user_data=validatedData.pop('user',{})
        user_obj,created=Profile.objects.get_or_create(**user_data)
        instance.user=user_obj
        instance.isPaid=validatedData.get('isPaid',instance.isPaid)
        instance.isDelivered=validatedData.get('isDelivered',instance.isDelivered)
        instance.save()
        return instance

class OrderItemSerializer(serializers.ModelSerializer):
    food=FoodSerializer(many=False)
    user=ProfileSerializer(many=False)
    order=OrderSerializer(many=False)
    class Meta:
        model = OrderItem
        fields = '__all__'

    def update(self,instance,validatedData):
        food=validatedData.pop('food',{})
        user=validatedData.pop('user',{})
        order=validatedData.pop('order',{})

        food_obj,created=Food.objects.get_or_create(**food)
        instance.food=food_obj

        user_obj,created=Profile.objects.get_or_create(**user)
        instance.user=user_obj

        order_obj,creadted=Order.objects.get_or_create(**order)
        instance.order=order_obj
        instance.qty=validatedData.get('qty',instance.qty)
        instance.save()
        
        return instance

