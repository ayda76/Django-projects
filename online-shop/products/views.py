from django.shortcuts import render,redirect
from .models import Product, Category, Review, Tag, Size,Color
from .utils import filterCat,filterColor,filterSize,filterTag, search, paginateProducts
from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage
from users.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import createProductForm,createColorForm,createCategoryForm,createReviewForm,createSizeForm,createTagForm

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
       
        

    custom_range,products=paginateProducts(request,products,3)

    context={'cats':cats,'tags':tags,'products':products, 'colors':colors, 'sizes':sizes, 'page':page, 'search_query':search_query,'custom_range':custom_range}
  
    return render(request,'products/shop.html',context)



@login_required(login_url='login')
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

        

        
############################# admin functions##################################


@login_required(login_url='login')
def createProduct(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    
    form=createProductForm()
    form_name='product'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createProductForm(request.POST,request.FILES)
            
            if form.is_valid():
                product_form=form.save(commit=False)
                product_form.owner=profile
                product_form.save()
                return redirect('admin-page')

    context={'form':form,'form_name':form_name}
    return render(request,'products/form.html',context)


@login_required(login_url='login')
def editProduct(request,pk):
    user=request.user
    product=Product.objects.get(id=pk)
    
    form=createProductForm(instance=product)
    form_name='edit_product'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createProductForm(request.POST,request.FILES,instance=product)
            
            if form.is_valid():
                form.save()
                return redirect('admin-page')

    context={'form':form,'form_name':form_name,'product':product}
    return render(request,'products/form.html',context)

@login_required(login_url='login') 
def deleteProduct(request,pk):
    user=request.user
    if user.is_staff == True:
        product=Product.objects.get(id=pk)
        product.delete()
       
        return redirect('admin-page')

######Tag Admin##########
@login_required(login_url='login')
def createTag(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    
    form=createTagForm()
    form_name='tag'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createTagForm(request.POST)
            if form.is_valid():
                tag_form=form.save(commit=False)
                alreadyExists=Tag.objects.filter(name=tag_form.name).exists()
                if alreadyExists == False:
                    tag_form.save()
                    return redirect('admin-page')
                
                

    context={'form':form,'form_name':form_name}
    return render(request,'products/form.html',context)

@login_required(login_url='login')
def editTag(request,pk):
    user=request.user
    tag=Tag.objects.get(id=pk)
    
    form=createTagForm(instance=tag)
    form_name='edit_tag'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createTagForm(request.POST,instance=tag)
            if form.is_valid():
                tag_form=form.save(commit=False)
                alreadyExists=Tag.objects.filter(name=tag_form.name).exists()
                if alreadyExists == False:
                    tag_form.save()
                    return redirect('admin-page')
                
                

    context={'form':form,'form_name':form_name,'tag':tag}
    return render(request,'products/form.html',context)


@login_required(login_url='login') 
def deleteTag(request,pk):
    user=request.user
    if user.is_staff == True:
        tag=Tag.objects.get(id=pk)
        
        tag.delete()
        return redirect('admin-page')


######Size Admin##########

@login_required(login_url='login')
def createSize(request):
    user=request.user
    
    form=createSizeForm()
    form_name='size'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createSizeForm(request.POST)
            if form.is_valid():
                
                size_form=form.save(commit=False)
                alreadyExists=Size.objects.filter(name=size_form.name).exists()
                if alreadyExists == False:
                    size_form.save()



                
                return redirect('admin-page')

    context={'form':form,'form_name':form_name}
    return render(request,'products/form.html',context)

@login_required(login_url='login')
def editSize(request,pk):
    user=request.user
    size=Size.objects.get(id=pk)
    
    form=createSizeForm(instance=size)
    form_name='edit_size'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createSizeForm(request.POST,instance=size)
            if form.is_valid():
                
                size_form=form.save(commit=False)
                alreadyExists=Size.objects.filter(name=size_form.name).exists()
                if alreadyExists == False:
                    size_form.save()
                    return redirect('admin-page')


    context={'form':form,'form_name':form_name,'size':size}
    return render(request,'products/form.html',context)

@login_required(login_url='login') 
def deleteSize(request,pk):
    user=request.user
    if user.is_staff == True:
        size=Size.objects.get(id=pk)
        
        size.delete()
        return redirect('admin-page')

########## Color Admin ###########
@login_required(login_url='login')
def createColor(request):
    user=request.user
    form=createColorForm()
    form_name='color'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createColorForm(request.POST,request.FILES)
            if form.is_valid():
                color_form=form.save(commit=False)
                alreadyExists=Color.objects.filter(name=color_form.name).exists()
                if alreadyExists == False:
                    color_form.save()
                    return redirect('admin-page')

    context={'form':form,'form_name':form_name}
    return render(request,'products/form.html',context)

@login_required(login_url='login')
def editColor(request,pk):
    user=request.user
    color=Color.objects.get(id=pk)
    
    form=createColorForm(instance=color)
    form_name='edit_color'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createColorForm(request.POST,request.FILES,instance=color)
            if form.is_valid():
                color_form=form.save(commit=False)
                alreadyExists=Color.objects.filter(name=color_form.name).exists()
                if alreadyExists == False:
                    color_form.save()
                    return redirect('admin-page')

    context={'form':form,'form_name':form_name,'color':color}
    return render(request,'products/form.html',context)

@login_required(login_url='login') 
def deleteColor(request,pk):
    user=request.user
    if user.is_staff == True:
        color=Color.objects.get(id=pk)
    
        color.delete()
        return redirect('admin-page')

#########Review Admin##########
@login_required(login_url='login')
def createReview(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    
    form=createReviewForm()
    form_name='review'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createReviewForm(request.POST)
            if form.is_valid():
                form.save()
                

                return redirect('admin-page')

    context={'form':form,'form_name':form_name}
    return render(request,'products/form.html',context)

@login_required(login_url='login')
def editReview(request,pk):
    user=request.user
    review=Review.objects.get(id=pk)
    form=createReviewForm(instance=review)
    form_name='edit_review'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createReviewForm(request.POST,instance=review)
            if form.is_valid():
                form.save()
                

                return redirect('admin-page')

    context={'form':form,'form_name':form_name,'review':review}
    return render(request,'products/form.html',context)

@login_required(login_url='login') 
def deleteReview(request,pk):
    user=request.user
    if user.is_staff == True:
        review=Review.objects.get(id=pk)
        
        review.delete()
        return redirect('admin-page')

#######Category Admin###########
@login_required(login_url='login')
def createCat(request):
    user=request.user
    form=createCategoryForm()
    form_name='cat'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createCategoryForm(request.POST,request.FILES)
            if form.is_valid():
                cat_form=form.save(commit=False)
                alreadyExists=Category.objects.filter(name=cat_form.name).exists()
                if alreadyExists == False:
                    cat_form.save()
                    return redirect('admin-page')
                return redirect('admin-page')

    context={'form':form,'form_name':form_name}
    return render(request,'products/form.html',context)


@login_required(login_url='login')
def editCat(request,pk):
    user=request.user
    cat=Category.objects.get(id=pk)
    form=createCategoryForm(instance=cat)
    form_name='edit_cat'
    if user.is_staff == True:
        
        if request.method == "POST":
            form=createCategoryForm(request.POST,request.FILES,instance=cat)
            if form.is_valid():
                cat_form=form.save(commit=False)
                alreadyExists=Category.objects.filter(name=cat_form.name).exists()
                if alreadyExists == False:
                    cat_form.save()
                    return redirect('admin-page')
                return redirect('admin-page')

    context={'form':form,'form_name':form_name,'cat':cat}
    return render(request,'products/form.html',context)

@login_required(login_url='login') 
def deleteCat(request,pk):
    user=request.user
    if user.is_staff == True:
        cat=Category.objects.get(id=pk)
        cat.delete()
        return redirect('admin-page')

    
