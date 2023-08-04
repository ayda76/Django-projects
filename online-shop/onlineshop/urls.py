from django.contrib import admin
from django.urls import path ,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
]
