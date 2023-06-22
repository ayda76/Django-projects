from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','description','demo_link','source_link','tags','featured_image']

    
    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)

        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})
        #self.fields['title'].widget.attrs.update({'class':'input'})