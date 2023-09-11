from django.db import models

from django.db import models
import uuid
# Create your models here.

class Ingredient(models.Model):
    name= models.CharField(max_length=300)
    created= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    def __str__(self):
        return self.name


class Food(models.Model):
    name= models.CharField(max_length=300)
    ing=models.ManyToManyField(Ingredient,null=True,blank=True)
    price=models.CharField(max_length=20,blank=True, null=True)
    image= models.ImageField(null=True, blank=True,upload_to='food/')
    discount=models.IntegerField(default=0,blank=True, null=True)
    
    created= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
     
    def __str__(self):
        return self.name
    
    @property
    def getDiscountPrice(self):
        self.price=self.price - (self.price * self.discount / 100)
        return self.price
        
    @property
    def imageURL(self):
        try:
            img=self.image.url

        except:
            img=''

        return img

    
