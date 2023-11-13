from django.db import models
import uuid
# Create your models here.

class Cat(models.Model):
    name=models.CharField(max_length=150,blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name=models.CharField(max_length=150,blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name

class Food(models.Model):
    name=models.CharField(max_length = 150,blank=True, null=True)
    ingredient= models.ManyToManyField(Ingredient,blank=True, null=True)
    cat=models.ForeignKey(Cat, on_delete=models.CASCADE,blank=True, null=True)
    price= models.CharField(max_length = 150,blank=True, null=True)
    image=models.ImageField(blank=True, null=True)
    onMenu= models.BooleanField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name

