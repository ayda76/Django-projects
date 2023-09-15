from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Food, Ingredient



class FoodForm(ModelForm):
    class Meta:
        model=Food
        fields='__all__'

    def  __init__(self,*args,**kwargs):
      

        super(FoodForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control','type':'text'})

            
class IngredientForm(ModelForm):
    class Meta:
        model=Ingredient
        fields='__all__'

    def  __init__(self,*args,**kwargs):
      

        super(IngredientForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control','type':'text'})            