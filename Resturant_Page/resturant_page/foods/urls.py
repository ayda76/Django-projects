from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.showMenu , name='menu'),
    path('', views.showHome , name='home'),
    
]