from django.urls import path
from . import views  # استيراد views من التطبيق المحلي

urlpatterns = [
    path('', views.Project_View.as_view(), name='project_list'),
    path('project/create', views.ProjectCreateView.as_view(), name='project_create'),
]