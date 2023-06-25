from django import forms
from django.forms import ModelForm,widgets
from .models import Project, Review
 


class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','description','demo_link','source_link','tags','featured_image']

    
    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})
        #self.fields['title'].widget.attrs.update({'class':'input'})


class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['body','value']
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }

    
    def __init__(self,*args,**kwargs):
        super(ReviewForm, self).__init__(*args,**kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})
       