from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Order, OrderItem



class orderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

    def  __init__(self,*args,**kwargs):
      

        super(orderForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control','type':'text'})

class orderitemForm(ModelForm):
    class Meta:
        model=OrderItem
        fields='__all__'

    def  __init__(self,*args,**kwargs):
      

        super(orderitemForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'form-control','type':'text'})