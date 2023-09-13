from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginUser, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.register, name='register'),
    path('update_user/',views.update_user, name='update_user'),

]