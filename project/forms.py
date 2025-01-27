from django import forms
from . import models

attrs = {'class' : 'form-control'}

class Project_Create_View(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'description': forms.Textarea(attrs={**attrs, 'rows': 3, 'style': 'resize: none;'}),  # تخصيص حقل الوصف
        }


    