from django.db import models
from users.models import Profile
from products.models import Product
import uuid
# Create your models here.



class Order(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    taxPrice=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    shippingPrice=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    paymentMethod=models.CharField(max_length=200,null=True,blank=True)
    isPaid=models.BooleanField(default=False)
    paidAt=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    isDelivered=models.BooleanField(default=False)
    deliveredAt=models.DateTimeField(auto_now_add=False,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    qty=models.IntegerField(null=True,blank=True,default=0)
    name=models.CharField(max_length=200,null=True,blank=True)
    price=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.name


