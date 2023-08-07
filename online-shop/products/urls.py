from django.urls import path ,include
from django.conf import settings
from . import views

urlpatterns = [
    
    
    path('',views.getProducts,name='products'),
    
    path('shop/',views.shop,name='shop'),
    path('<str:pk>/',views.getProduct,name='product'),
    
    
    
]