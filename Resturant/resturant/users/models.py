from django.db import models
from django.contrib.auth.models import User
from food.models import Food
import uuid
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length = 150, blank=True, null=True)
    firstname=models.CharField(max_length=200,blank=True, null=True)
    lastname=models.CharField(max_length=200, blank=True, null=True)
    address=models.TextField()
    phone=models.CharField(max_length = 11, blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.username
    

class Review(models.Model):
    owner=models.ForeignKey(Profile, on_delete=models.CASCADE)
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    comment=models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.created)

    

    
    
    