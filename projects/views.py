from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy 
from . import models
from . import forms

# Create your views here.


class Project_View(ListView):
    model = models.Project
    template_name = 'project/list_view.html'

class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.Project_Create_View
    template_name = 'project/create_view.html'
    success_url = reverse_lazy('project_list')