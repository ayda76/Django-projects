from django.contrib import admin
from .models import Product,Review, Category, Tag,Size,Color
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Size)
admin.site.register(Color)