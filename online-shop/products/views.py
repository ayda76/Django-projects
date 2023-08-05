from django.shortcuts import render
from .models import Product, Category, Review, Tag
# Create your views here.

def getProducts(request):
    products=Product.objects.all()
    slider_products=Product.objects.filter(vote_ratio__gte=4)
    cats=Category.objects.all()
    tags=Tag.objects.all()

    context={'products':products,'slider_products':slider_products,'cats':cats, 'tags':tags }
    return render(request, 'products/products.html',context)


def getProduct(request,pk):
    product=Product.objects.get(id=pk)
    products=Product.objects.all()
    cats=Category.objects.all()
    tags=Tag.objects.all()
    
    context={'product':product,'cats':cats,'tags':tags,'products':products}
    return render(request,'products/product.html',context)


def shop(request):
    products=Product.objects.all()
    cats=Category.objects.all()
    tags=Tag.objects.all()


    context={'cats':cats,'tags':tags,'products':products}
    return render(request,'products/shop.html',context)
