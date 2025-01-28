from django import forms
from . import models
from django.utils.translation import gettext_lazy as _

attrs = {'class' : 'form-control'}

class Project_Create_View(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        labels = {  
            'category':_('Category'),
            'title':_('Title'),
            'description':_('Description'),
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs={**attrs, 'rows': 3, 'style': 'resize: none;'}),  # تخصيص حقل الوصف
        }

class Project_Update_View(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'projectstatus']
        labels = {  
            'category':_('Category'),
            'title':_('Title'),
            'projectstatus':_('Projectstatus'),
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'projectstatus': forms.Select(attrs=attrs),
        }



    