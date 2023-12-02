from django.db import models
from users.models import Profile
from foods.models import Food
# Create your models here.

class Order(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    isPaid= models.BooleanField(blank=True, null=True)
    isDelivered= models.BooleanField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.created)

    def totalPrice(self):
        total=self.food.price * self.qty
        return total
