from django.forms import ModelForm
from django.contrib.auth.models import User
from users.models import Profile
from .models import Product, Tag,Size,Category,Color, Review


class createProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'


class createCategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'



class createTagForm(ModelForm):
    class Meta:
        model=Tag
        fields='__all__'

class createColorForm(ModelForm):
    class Meta:
        model=Color
        fields='__all__'

class createSizeForm(ModelForm):
    class Meta:
        model=Size
        fields='__all__'

class createReviewForm(ModelForm):
    class Meta:
        model=Review
        fields='__all__'

class editProductForm(ModelForm):
    class Meta:
        model=Product
        fields='__all__'       