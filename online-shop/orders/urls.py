from django.urls import path ,include
from django.conf import settings
from . import views

urlpatterns=[
    path('checkout/',views.viewCheckout, name='checkout'),
    path('delete_order/<str:pk>/',views.deleteOrderItem, name='delete_order'),
    path('update_orderItem/<str:pk>/',views.updateOrder, name='update_orderItem'),
    path('submit_order/<str:pk>/',views.submitOrder, name='submit_order'),
    path('',views.getOrders, name='orders'),
    
    
]