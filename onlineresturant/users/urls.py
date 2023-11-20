from django.contrib import admin
from django.urls import path
import views as views

urlpatterns = [
    path('getUsers/',views.getUsers, name='getUsers'),
    path('getUserById/<str:pk>',views.getUserById, name='getUserById'),
    path('addOrder/',views.addOrder,name='addOrder'),
    path('updateUser/<str:pk>',views.updateUser,name='updateUser'),
    path('deleteUser/<str:pk>',views.deleteUser,name='deleteUser'),
    path('loginUser/<str:pk>',views.loginUser,name='loginUser'),
    path('signupUser/',views.signupUser,name='signupUser')
]