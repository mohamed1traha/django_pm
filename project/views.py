from django.shortcuts import render
from . import models
from . import forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Project_View(LoginRequiredMixin, ListView):
    model = models.Project
    template_name = 'project/list.html'
    paginate_by = 3
        
    def get_queryset(self):
        query_set = super().get_queryset()
        where = {'user_id': self.request.user}
        q = self.request.GET.get('q', None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.Project_Create_View
    template_name = 'project/create_view.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Projectupdateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Project
    form_class = forms.Project_Update_View
    template_name = 'project/update_view.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])
    

class ProjectDeletView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Project
    template_name = 'project/delete_view.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.get_object().user == self.request.user


class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.Task
    fields = ['project', 'description']
    template_name = 'project/task_create_view.html'
    http_method_names = ['post']

    def test_func(self):
        project_id = self.request.POST.get('project', '')
        return models.Project.objects.get(pk=project_id).user == self.request.user

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Task
    fields = ['is_completed']

    def test_func(self):
        return self.get_object().project.user == self.request.user
    
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


class TaskDeletView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Task

    def test_func(self):
        return self.get_object().project.user == self.request.user

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
