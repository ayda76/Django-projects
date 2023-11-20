from django.contrib import admin
from django.urls import path
import .views as views

urlpatterns = [
    path('getFoods/',views.getFoods, name='getFood'),
    path('getFoodById/<str:pk>',views.getFoodById, name='getFoodById'),
    path('addFood/',views.addFood,name='addFood'),
    path('updateFood/<str:pk>',views.updateFood,name='updateFood'),
    path('deleteFood/<str:pk>',views.deleteFood,name='deleteFood'),
    path('getCats/',views.getCat,name='getCat'),
    path('getCatById/<str:pk>',views.getCatById, name='getCatById'),
    path('addCat/',views.addCat,name='addCat'),
    path('updateCat/<str:pk>',views.updateCat,name='updateCat'),
    path('deleteCat/<str:pk>',views.deleteCat,name='deleteCat'),
    path('getIngredients/',views.getIngredient,name='getIngredient'),
    path('getIngredientById/<str:pk>',views.getIngredientById, name='getIngredientById'),
    path('addIngredient/',views.addIngredient,name='addIngredient'),
    path('updateIngredient/<str:pk>',views.updateIngredient,name='updateIngredient'),
    path('deleteIngredient/<str:pk>',views.deleteIngredient,name='deleteIngredient'),
]