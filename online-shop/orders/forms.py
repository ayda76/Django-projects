from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Order,OrderItem

          
class createOrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'
    def  __init__(self,*args,**kwargs):
        super(createOrderForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text checkout-content'})

class createOrderItemForm(ModelForm):
    class Meta:
        model=OrderItem
        fields='__all__'

    def  __init__(self,*args,**kwargs):
        super(createOrderItemForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text checkout-content'})