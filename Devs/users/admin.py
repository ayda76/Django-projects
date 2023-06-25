from django.contrib import admin
from .models import Profile, skills, Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(skills)
admin.site.register(Message)