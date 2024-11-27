from django.urls import path
from . import views  # استيراد views من التطبيق المحلي

urlpatterns = [
    path('', views.projects, name='index'),  # تأكد من وجود view صالح مرتبط بهذا المسار
]