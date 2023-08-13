from django.urls import path ,include
from django.conf import settings
from . import views

urlpatterns = [
    
    
    path('edit-product/<str:pk>/',views.editProduct,name='edit-product'),
    path('edit-tag/<str:pk>/',views.editTag,name='edit-tag'),
    path('edit-color/<str:pk>/',views.editColor,name='edit-color'),
    path('edit-size/<str:pk>/',views.editSize,name='edit-size'),
    path('edit-cat/<str:pk>/',views.editCat,name='edit-cat'),
    path('edit-review/<str:pk>/',views.editReview,name='edit-review'),

    path('create-product/',views.createProduct,name='create-product'),
    path('create-tag/',views.createTag,name='create-tag'),
    path('create-color/',views.createColor,name='create-color'),
    path('create-size/',views.createSize,name='create-size'),
    path('create-cat/',views.createCat,name='create-cat'),
    path('create-review/',views.createReview,name='create-review'),


   


    path('delete-product/<str:pk>/',views.deleteProduct,name='delete-product'),
    path('delete-tag/<str:pk>/',views.deleteTag,name='delete-tag'),
    path('delete-color/<str:pk>/',views.deleteColor,name='delete-color'),
    path('delete-size/<str:pk>/',views.deleteSize,name='delete-size'),
    path('delete-cat/<str:pk>/',views.deleteCat,name='delete-cat'),
    path('delete-review/<str:pk>/',views.deleteReview,name='delete-review'),

    path('',views.getProducts,name='products'),
    
    path('shop/',views.shop,name='shop'),
    path('createReviews/<str:pk>/',views.createReviews,name='createReviews'),
    path('<str:pk>/',views.getProduct,name='product'),

    
    
    
    
]