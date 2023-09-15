from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.register, name='register'),
    path('update_user/',views.update_user, name='update_user'),

    path('admin-user-create/', views.create_User, name='admin-user-create'),
    path('admin-user-update/<str:pk>', views.update_User , name='admin-user-update'),
    path('admin-user-delete/<str:pk>', views.delete_User , name='admin-user-delete'),
    path('admin-user/', views.read_User, name='admin-user-page'),

    path('admin-review-create/', views.create_Review, name='admin-review-create'),
    path('admin-review-update/<str:pk>', views.update_Review , name='admin-review-update'),
    path('admin-review-delete/<str:pk>', views.delete_Review , name='admin-review-delete'),
    path('admin-review/', views.read_Review, name='admin-review-page'),

]