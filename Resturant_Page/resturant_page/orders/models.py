from django.db import models
from foods.models import Food
from users.models import Profile
import uuid
# Create your models here.

class Order(models.Model):
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    isPaid=models.BooleanField(default=False)
    paymentMethod=models.CharField(max_length=200,default='paypal')
    paidAt=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    isDelivered=models.BooleanField(default=False)
    deliveredAt=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.created)
    
    

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    food_item=models.ForeignKey(Food, on_delete=models.CASCADE)
    qty=models.IntegerField(blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

   

    def __str__(self):
        return str(self.created)

    @property
    def getPrice(self):
        price=self.qty * int(self.food_item.price)
        return price
    
    


