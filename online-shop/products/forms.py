from django.forms import ModelForm
from django.contrib.auth.models import User
from users.models import Profile
from .models import Product, Tag,Size,Category,Color, Review


class createProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'

    def  __init__(self,*args,**kwargs):
        super(createProductForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text checkout-content'})


class createCategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'
    def  __init__(self,*args,**kwargs):
        super(createCategoryForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text checkout-content'})



class createTagForm(ModelForm):
    class Meta:
        model=Tag
        fields='__all__'
    def  __init__(self,*args,**kwargs):
        super(createTagForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text checkout-content'})

class createColorForm(ModelForm):
    class Meta:
        model=Color
        fields='__all__'
    def  __init__(self,*args,**kwargs):
        super(createColorForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text checkout-content'})

class createSizeForm(ModelForm):
    class Meta:
        model=Size
        fields='__all__'

    def  __init__(self,*args,**kwargs):
        super(createSizeForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text checkout-content'})

class createReviewForm(ModelForm):
    class Meta:
        model=Review
        fields='__all__'
    def  __init__(self,*args,**kwargs):
        super(createReviewForm, self).__init__(*args,**kwargs)
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input input--text checkout-content'})

