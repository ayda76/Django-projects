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

    path('admin-order-create/', views.create_order, name='admin-order-create'),
    path('admin-order-update/<str:pk>', views.update_order , name='admin-order-update'),
    path('admin-order-delete/<str:pk>', views.delete_order , name='admin-order-delete'),
    path('admin-order/', views.read_order, name='admin-order-page'),

    path('admin-orderitem-create/', views.create_orderitem, name='admin-orderitem-create'),
    path('admin-orderitem-update/<str:pk>', views.update_orderitem , name='admin-orderitem-update'),
    path('admin-orderitem-delete/<str:pk>', views.delete_orderitem , name='admin-orderitem-delete'),
    path('admin-orderitem/', views.read_orderitem, name='admin-orderitem-page'),
    
  
]