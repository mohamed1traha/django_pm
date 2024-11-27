from django import forms
from . import models

class Project_Create_View(forms.ModelForm):
    class Meta :
        model = models.Project
        fields = ['category', 'title','description']
        widgets = {
            'category' : forms.Select(),   
            'title' : forms.TextInput(),   
            
        }
     