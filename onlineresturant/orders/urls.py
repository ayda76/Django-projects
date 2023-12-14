from django.contrib import admin
from django.urls import path
from . import views as views

urlpatterns = [
    
    path('addOrder/',views.addOrder,name='addOrder'),
    path('addOrderItem/',views.addOrderItem,name='addOrderItem'),
    path('getAllOrderItems/',views.getAllOrderItems, name='getAllOrderItems'),
    path('updateOrder/<str:pk>',views.updateOrder,name='updateOrder'),
    path('updateOrderItemQTY/<str:pk>',views.updateOrderItemQTY,name='updateOrderItemQTY'),
    path('deleteOrder/<str:pk>',views.deleteOrder,name='deleteOrder'),
    path('deleteOrderItem/<str:pk>',views.deleteOrderItem,name='deleteOrderItem'),
    path('getOrderItem/<str:pk>',views.getOrderItem, name='getOrderItem'),
    
    
    path('<str:pk>',views.getOrderById, name='getOrderById'),
    path('',views.getOrders, name='getOrder'),
    
    
    
]
#path('updateOrderItemQTY/<str:pk>',views.updateOrderItemQTY,name='updateOrderItemQTY'),