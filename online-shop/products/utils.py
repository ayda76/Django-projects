from .models import Product, Tag, Category, Review, Size,Color
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage


def search(request):
    search_query=''
    if request.GET.get('search_query'):
        search_query= request.GET.get('search_query')

    tag=Tag.objects.filter(name__icontains=search_query)
    size=Size.objects.filter(name__icontains=search_query)
    cat=Category.objects.filter(name__icontains=search_query)

    products= Product.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(brand__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(tag__in=tag)|
        Q(cat__in=cat) |
        Q(size__in=size) 
    )

    return products, search_query

def filterCat(pk):
    cat=Category.objects.get(id=pk)
    products=Product.objects.filter(cat=cat)
    

    return products

def filterTag(pk):
    tag=Tag.objects.get(id=pk)
    products=Product.objects.filter(tag=tag)

    return products

def filterColor(pk):
    color=Color.objects.get(id=pk)
    products=Product.objects.filter(color=color)

    return products

def filterSize(pk):
    size=Size.objects.get(id=pk)
    products=Product.objects.filter(size=size)

    return products


def paginateProducts(request,products, results):
    page=request.GET.get('page')
    
    paginator=Paginator(products,results)
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        page=1
        products=paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        products=paginator.page(page)

    
    leftIndex=(int(page)-4)
    if leftIndex < 1:
        leftIndex =1
    rightIndex=(int(page)+5)
    if rightIndex > paginator.num_pages:
        rightIndex=paginator.num_pages+1

    custom_range =range(leftIndex,rightIndex)
    

    return custom_range,products
