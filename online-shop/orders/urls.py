from django.urls import path ,include
from django.conf import settings
from . import views

urlpatterns=[
    path('',views.getOrders, name='orders'),
    path('make-order/<str:pk>',views.makeOrder, name='make-order')
]