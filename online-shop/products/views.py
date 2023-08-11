from django.shortcuts import render,redirect
from .models import Product, Category, Review, Tag, Size,Color
from .utils import filterCat,filterColor,filterSize,filterTag, search
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from users.models import Profile
from django.contrib import messages
# Create your views here.




def getProducts(request):
    page=False
    search_query=''
    products=Product.objects.all()
    slider_products=Product.objects.filter(vote_ratio__gte=4)
    cats=Category.objects.all()
    tags=Tag.objects.all()
    
    context={'products':products,'slider_products':slider_products,'cats':cats, 'tags':tags, 'page':page,'search_query':search_query }
    return render(request, 'products/products.html',context)


def getProduct(request,pk):
    page=True
    product=Product.objects.get(id=pk)
    products=Product.objects.all()
    cats=Category.objects.all()
    tags=Tag.objects.all()
    colors=Color.objects.all()
    sizes=Size.objects.all()
    
    
    context={'product':product,'cats':cats,'tags':tags,'products':products, 'colors':colors, 'sizes':sizes, 'page':page}
    return render(request,'products/product.html',context)

def shop(request):
    #get the filter and id of filter
    q= request.GET.get('q') if request.GET.get('q') !=None else ''
    q=q.split(",")

    page=True
    
    cats=Category.objects.all()
    tags=Tag.objects.all()
    colors=Color.objects.all()
    sizes=Size.objects.all()
  
    if q[0] == 'cat':
        cat=Category.objects.get(id=q[1])
        search_query=cat.name
        products=filterCat(pk=q[1])

    elif q[0] == 'size':
        size=Size.objects.get(id=q[1])
        search_query=size.name
        products=filterSize(pk=q[1])

    elif q[0] == 'color':
        color=Color.objects.get(id=q[1])
        search_query=color.name
        products=filterColor(pk=q[1])

    elif q[0] == 'tag':
        tag=Tag.objects.get(id=q[1])
        search_query=tag.name
        products=filterTag(pk=q[1])
        
    else:

        if request.GET.get('search_query'):
            
            products,search_query=search(request)
        
        else:
            search_query=''
            products=Product.objects.all()
       
        

    #custom_range,products=paginateProjects(request,products,3)

    context={'cats':cats,'tags':tags,'products':products, 'colors':colors, 'sizes':sizes, 'page':page, 'search_query':search_query}
  
    return render(request,'products/shop.html',context)




def createReviews(request,pk):
    product=Product.objects.get(id=pk)
    user=request.user
    profile=Profile.objects.get(user=user)

    if profile.review_set.filter(product=product):
        messages.error(request,'you have already commented on this product!')
        return redirect('product',pk=product.id)
       

    else:
        if request.method == 'POST':
            rating=request.POST['rating']
            comment=request.POST['comment']
        
         
            new_review=Review.objects.create(
                owner=profile,
                product=product,
                rating=rating,
                comment=comment)
            

            reviews=product.review_set.all()
            total=0
            for i in reviews:
                total += i.rating
            

            product.rating=total / len(reviews)   
            product.save()

            return redirect('product',pk=product.id)

        

        

    

    
