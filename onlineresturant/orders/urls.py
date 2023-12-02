from django.contrib import admin
from django.urls import path
from . import views as views

urlpatterns = [
    path('',views.getOrders, name='getOrder'),
    path('<str:pk>',views.getOrderById, name='getOrderById'),
    path('addOrder/',views.addOrder,name='addOrder'),
    path('updateOrder/<str:pk>',views.updateOrder,name='updateOrder'),
    path('deleteOrder/<str:pk>',views.deleteOrder,name='deleteOrder'),
    path('getAllOrderItems/',views.getAllOrderItems, name='getAllOrderItems'),
    path('getOrderItem/<str:pk>',views.getOrderItem, name='getOrderItem'),
    path('addOrderItem/',views.addOrderItem,name='addOrderItem'),
    path('updateOrderItemQTY/<str:pk>',views.updateOrderItemQTY,name='updateOrderItemQTY'),
    path('deleteOrderItem/<str:pk>',views.deleteOrderItem,name='deleteOrderItem'),
]