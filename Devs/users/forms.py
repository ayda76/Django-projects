from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields=['first_name', 'email','username','password1','password2']
        labels={'first_name':'name'}

        def __init__(self,*args,**kwargs):
            super(CustomUserCreationForm, self).__init__(*args,**kwargs)

            for key, value in self.fields.items():
                value.widget.attrs.update({'class':'input input--text'})
            

        

        