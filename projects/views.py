from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView  ,UpdateView, DeleteView
from django.urls import reverse_lazy ,reverse
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

class Projectupdateview(UpdateView):
    model = models.Project
    form_class = forms.Project_Update_View
    template_name = 'project/update_view.html'
    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])
    

class ProjectDeletView(DeleteView):
    model = models.Project
    template_name = 'project/delete_view.html'
    success_url = reverse_lazy('project_list')

    

class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    template_name = 'project/task_create_view.html'
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])



class TaskDeletView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


