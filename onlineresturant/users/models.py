from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=150,blank=True, null=True)
    lasttname=models.CharField(max_length=150,blank=True, null=True)
    address=models.TextField()
    tel=models.CharField(max_length=11,blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name
    