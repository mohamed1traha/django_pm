from django.shortcuts import render
from . import models
from . import forms
from django.views.generic import ListView, CreateView  ,UpdateView, DeleteView
from django.urls import reverse_lazy ,reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.

class Project_View(LoginRequiredMixin,ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 3
        
    def get_queryset(self) :
        query_set= super().get_queryset()
        where= {}
        q= self.request.GET.get('q',None)
        if q : where['title__icontains'] =q
        return query_set.filter(**where)


class ProjectCreateView(CreateView,LoginRequiredMixin):
    model = models.Project
    form_class = forms.Project_Create_View
    template_name = 'project/create_view.html'
    success_url = reverse_lazy('project_list')


class Projectupdateview(UpdateView,LoginRequiredMixin):
    model = models.Project
    form_class = forms.Project_Update_View
    template_name = 'project/update_view.html'
    success_url = reverse_lazy('project_list')

    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])
    

class ProjectDeletView(DeleteView,LoginRequiredMixin):
    model = models.Project
    template_name = 'project/delete_view.html'
    success_url = reverse_lazy('project_list')

    

class TaskCreateView(CreateView,LoginRequiredMixin):
    model = models.Task
    fields = ['project', 'description']
    template_name = 'project/task_create_view.html'
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])

class TaskUpdateView(UpdateView,LoginRequiredMixin):
    model = models.Task
    fields = ['is_completed']
    
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskDeleteView(DeleteView,LoginRequiredMixin):
    model = models.Task

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
