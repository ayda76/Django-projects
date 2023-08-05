from django.urls import path ,include
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.getUsers, name='users'),
    path('/login/',views.login, name='login'),
    
]