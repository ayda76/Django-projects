from django.contrib import admin
from .models import Food, Cat, Ingredient
# Register your models here.
admin.site.register(Food)
admin.site.register(Cat)
admin.site.register(Ingredient)