from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', views.showMenu , name='menu'),
    path('create-review', views.createReview , name='create-review'),
    path('food/<str:pk>', views.showFood , name='food'),
    path('', views.showHome , name='home'),
    
]