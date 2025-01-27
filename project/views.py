from django.shortcuts import render
from . import models
from . import forms
from django.views.generic import ListView, CreateView  ,UpdateView, DeleteView
from django.urls import reverse_lazy ,reverse


# Create your views here.

class Project_View(ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 6

class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.Project_Create_View
    template_name = 'project/create_view.html'
    success_url = reverse_lazy('project_list')