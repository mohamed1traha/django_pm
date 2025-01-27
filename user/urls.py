from django.urls import path, include
  # استيراد views من التطبيق المحلي
from django.contrib.auth.views import LoginView
from user.views import RegisterView,edit_profile
from user.forms import UserLoginForm


urlpatterns = [
    path('', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path ('', include('django.contrib.auth.urls'))
    
]
