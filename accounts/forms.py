from django.contrib.auth.forms import AuthenticationForm, UserCreationForm ,UserChangeForm
from django import forms
from django.contrib.auth.models import User

# إعدادات مشتركة للحقل
attrs = {'class': 'form-control'}

# نموذج تسجيل الدخول
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs)
    )

# نموذج تسجيل المستخدم
class UseRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name',
        widget=forms.TextInput(attrs=attrs)
    )
    last_name = forms.CharField(
        label='Last Name',
        widget=forms.TextInput(attrs=attrs)
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs=attrs)
    )
    email = forms.EmailField(  # إصلاح الحقل ليكون email
        label='Email',
        widget=forms.EmailInput(attrs=attrs)
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs=attrs)
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs=attrs)
    )

    class Meta:
        model = User  # ربط النموذج بنموذج User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class ProfileForm(UserChangeForm) :
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name':forms.TextInput(attrs=attrs),
            'last_name':forms.TextInput(attrs=attrs),
            'email':forms.EmailInput(attrs=attrs),
            'username':forms.TextInput(attrs=attrs),
            }
        




