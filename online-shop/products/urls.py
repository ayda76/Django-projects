from django.urls import path ,include
from django.conf import settings
from . import views

urlpatterns = [
    
    
    path('create-product/',views.createProduct,name='create-product'),
    path('create-tag/',views.createTag,name='create-tag'),
    path('create-color/',views.createColor,name='create-color'),
    path('create-size/',views.createSize,name='create-size'),
    path('create-cat/',views.createCat,name='create-cat'),
    path('create-review/',views.createReview,name='create-review'),

    path('',views.getProducts,name='products'),
    
    path('shop/',views.shop,name='shop'),
    path('createReviews/<str:pk>/',views.createReviews,name='createReviews'),
    path('<str:pk>/',views.getProduct,name='product'),

    
    
    
    
]