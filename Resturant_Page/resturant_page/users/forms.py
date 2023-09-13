from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class registerUser(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name' ,'username','password1','password2']

    def  __init__(self,*args,**kwargs):
      

        super(registerUser, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control','type':'text'})
            #form-group wow fadeInDown


class updateUserForm(ModelForm):
    class Meta:
        model=Profile
        fields= '__all__'

    def  __init__(self,*args,**kwargs):
      

        super(updateUserForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control','type':'text'})

