from django.urls import path ,include
from django.conf import settings
from . import views

urlpatterns=[

    path('delete-order-admin/<str:pk>/',views.deleteOrderAdmin,name='delete-order-admin'),
    path('delete-orderitem-admin/<str:pk>/',views.deleteOrderItemAdmin,name='delete-orderitem-admin'),
    
    path('edit-order/<str:pk>/',views.editOrder,name='edit-order'),
    path('edit-orderitem/<str:pk>/',views.editOrderItem,name='edit-orderitem'),

    path('create-order/',views.createOrder,name='create-order'),
    path('create-orderitem/',views.createOrderItem,name='create-orderitem'),



    path('checkout/',views.viewCheckout, name='checkout'),
    path('delete_order/<str:pk>/',views.deleteOrderItem, name='delete_order'),
    path('update_orderItem/<str:pk>/',views.updateOrder, name='update_orderItem'),
    path('submit_order/<str:pk>/',views.submitOrder, name='submit_order'),
    path('',views.getOrders, name='orders'),
    
    
]