from django.urls import path ,include
from django.conf import settings
from . import views
urlpatterns = [
    path('update-profile/',views.updateProfile, name='update-profile'),
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerUser, name='register'),
    path('admin-page/',views.getAdminPages, name='admin-page'),
    path('',views.getUsers, name='users'),
    
    
]