from django.urls import path, include
  # استيراد views من التطبيق المحلي
from django.contrib.auth.views import LoginView
from accounts.views import RegisterView,edit_profile


urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path ('', include('django.contrib.auth.urls'))
    
]
