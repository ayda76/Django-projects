from django.db import models
from users.models import Profile
import uuid

from colorfield.fields import ColorField
# Create your models here.

#tags model
class Tag(models.Model):
    name=models.CharField(max_length=300)  
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

# Category model 
class Category(models.Model):
    name=models.CharField(max_length=300) 
    image=models.ImageField(upload_to='cat-img/',default='/staticfiles/images/latest-1.jpg')
    Banner=models.ImageField(upload_to='cat-img/banner/',default='/staticfiles/images/latest-1.jpg')
     
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name   

    @property 
    def imageURL(self):
        try:
            img=self.image.url

        except:
            img=''

        return img

#size model
class Size(models.Model):
    name=models.CharField(max_length=10)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


#color model
class Color(models.Model):
    color = ColorField(default='#FFFFFF')
    name=models.CharField(max_length=300, default='white', null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


#product model
class Product(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    tag=models.ForeignKey(Tag,null=True,blank=True,on_delete=models.SET_NULL)
    cat=models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)
    size=models.ManyToManyField(Size,null=True,blank=True)
    color=models.ManyToManyField(Color,null=True,blank=True)
    
    name=models.CharField(max_length=300)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True, blank=True,upload_to='profiles/')
    brand=models.CharField(max_length = 150,null=True,blank=True)

    price=models.FloatField(default=0, null=True, blank=True)
    discount=models.IntegerField(default=0, null=True, blank=True)
    stock=models.IntegerField(default=0, null=True, blank=True)

    vote_total=models.IntegerField(default=0, null=True, blank=True)
    vote_ratio=models.IntegerField(default=0,null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    @property 
    def imageURL(self):
        try:
            img=self.image.url

        except:
            img=''

        return img

    @property 
    def getVoteCount(self):
        reviews=self.review_set.all()
        upVotes=reviews.filter(value='up').count()
        total=reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()


    @property 
    def getPriceWithDiscount(self):
        if self.discount != 0:
            price=self.price - self.price * self.discount /100
            print(price)
            return price
            

        

        







#Reviews model
class Review(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    VOTE_TYPE=(
        ('up','up_vote'),
        ('down','down_vote')
    )
    value=models.CharField(max_length = 200, choices=VOTE_TYPE)
    comment=models.TextField(null=True, blank=True) 
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
    
