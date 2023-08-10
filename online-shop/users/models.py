from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    first_name=models.CharField(max_length=400)
    last_name=models.CharField(max_length=400)
    username=models.CharField(max_length=200,null=True, blank=True)
    #password=models.make_password()
    image=models.ImageField(null=True, blank=True,upload_to='profiles/')
    tel=models.CharField(max_length=11)
    email=models.EmailField(max_length=400,null=True, blank=True)
    postalcode=models.CharField(max_length=15)
    country=models.TextField(null=True, blank=True)
    city=models.TextField(null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id= models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.username
    
    def getImageURL(self):
        try:
            img=self.image.url

        except:
            img=''

        return img

