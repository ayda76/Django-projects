from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.showMenu , name='menu'),
    path('create-review', views.createReview , name='create-review'),
    path('food/<str:pk>', views.showFood , name='food'),
    path('', views.showHome , name='home'),

    path('admin-food-create/', views.create_Food , name='admin-food-create'),
    path('admin-food-update/<str:pk>', views.update_Food , name='admin-food-update'),
    path('admin-food-delete/<str:pk>', views.delete_Food , name='admin-food-delete'),
    path('admin-page/', views.read_Food , name='admin-page'),

    path('admin-ingredient-create/', views.create_Ingredient , name='admin-ingredient-create'),
    path('admin-ingredient-update/<str:pk>', views.update_Ingredient , name='admin-ingredient-update'),
    path('admin-ingredient-delete/<str:pk>', views.delete_Ingredient , name='admin-ingredient-delete'),
    path('admin-ingredient-page/', views.read_Ingredient , name='admin-ingredient-page'),
    
]