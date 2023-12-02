from django.contrib import admin
from django.urls import path
from . import views as views

urlpatterns = [
    
    path('addFood/',views.addFood,name='addFood'),
    path('addCat/',views.addCat,name='addCat'),
    path('addIngredient/',views.addIngredient,name='addIngredient'),
    path('updateFood/<str:pk>',views.updateFood,name='updateFood'),
    path('updateIngredient/<str:pk>',views.updateIngredient,name='updateIngredient'),
    path('deleteFood/<str:pk>',views.deleteFood,name='deleteFood'),
    path('getCats/',views.getCats,name='getCats'),
    path('getIngredients/',views.getIngredients,name='getIngredients'),
    path('updateCat/<str:pk>',views.updateCat,name='updateCat'),
    path('getCatById/<str:pk>',views.getCatById, name='getCatById'),
    path('',views.getFoods, name='getFoods'),
    path('<str:pk>/',views.getFoodById, name='getFoodById'),
    path('deleteCat/<str:pk>',views.deleteCat,name='deleteCat'),
    
    path('getIngredientById/<str:pk>',views.getIngredientById, name='getIngredientById'),
    
    
    path('deleteIngredient/<str:pk>',views.deleteIngredient,name='deleteIngredient'),
]