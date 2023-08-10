from django.shortcuts import render
from .models import Product, Category, Review, Tag, Size,Color
from .utils import filterCat,filterColor,filterSize,filterTag, search
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
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





