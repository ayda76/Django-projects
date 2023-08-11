from django.urls import path ,include
from django.conf import settings
from . import views

urlpatterns = [
    
    
    path('',views.getProducts,name='products'),
    
    path('shop/',views.shop,name='shop'),
    path('createReviews/<str:pk>/',views.createReviews,name='createReviews'),
    path('<str:pk>/',views.getProduct,name='product'),
    
    
    
]