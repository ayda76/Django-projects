from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('create-order/<str:pk>',views.createOrders, name='create-order'),
    path('delete-order/<str:pk>',views.deleteOrderItem, name='delete-order'),
    path('update-order/<str:pk>',views.updateOrderItem, name='update-order'),
    path('',views.showOrderItems, name='orders'),
    
    path('pay-order/<str:pk>',views.paybill, name='pay-order'),
    
    path('make-order/',views.makeOrder, name='make-order'),
    
  
]