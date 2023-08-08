from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class registerUserProfileForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name' ,'email','username','password1','password2']

    def  __init__(self,*args,**kwargs):
      

        super(registerUserProfileForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text'})