from django.shortcuts import render
from .models import Product, Category, Review
# Create your views here.

def getProducts(request):
    products=Product.objects.all()
    slider_products=Product.objects.filter(vote_ratio__gte=4)
    cats=Category.objects.all()
    context={'products':products,'slider':slider_products[:4],'cats':cats}
    return render(request, 'products/products.html',context)


