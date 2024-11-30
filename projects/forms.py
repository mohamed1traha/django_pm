from django import forms
from . import models
from django. utils.translation import gettext as _

# تعريف الفئة المشتركة للاستخدام في الحقول
attrs = {'class' : 'form-control'}

class Project_Create_View(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['category', 'title', 'description']
        lable = {
            'category':_('category'),
            'title':_('title'),
            'description': _('description'),
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
        lable = {
            'category':_('category'),
            'title':_('title'),
            'projectstatus': _('projectstatus'),
        }
        widgets = {
            'category': forms.Select(attrs=attrs),
            'title': forms.TextInput(attrs=attrs),
            'projectstatus': forms.Select(attrs=attrs),
        }
