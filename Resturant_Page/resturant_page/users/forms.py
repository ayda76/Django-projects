from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class registerUser(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name' ,'email','username','password1','password2']