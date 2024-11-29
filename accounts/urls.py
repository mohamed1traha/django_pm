from django.urls import path, include
from . import views  # استيراد views من التطبيق المحلي
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path ('', include('django.contrib.auth.urls'))
]
