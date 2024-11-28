from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView  ,UpdateView, DeleteView
from django.urls import reverse_lazy ,reverse
from . import models
from . import forms

# Create your views here.


# لعرض المشاريع الموجود 
class Project_View(ListView):
    model = models.Project
    template_name = 'project/list_view.html'


# دالة انشاء المشاريع 
class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.Project_Create_View
    template_name = 'project/create_view.html'
    # متغير ثابت 
    # سيستخدم عند عدم الحاجة الى استخدام اي دي المشروع 
    success_url = reverse_lazy('project_list')


#دالة تعديل المشاريع 
class Projectupdateview(UpdateView):
    model = models.Project
    form_class = forms.Project_Update_View
    template_name = 'project/update_view.html'
    # دالة التوجيه 
    #تستخدم عند الحاجة الى الحصول ال ايدي  مشروع معين 
    # حيق يتم التوجيه الى الصفحة نفسها  بعد التتعديل 
    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])
    
# دالة حذف المشاريع 
class ProjectDeletView(DeleteView):
    model = models.Project
    template_name = 'project/delete_view.html'
    # لم يتم استخدام الدالة لاننها هنا لم نحتج الى الحصول على اي دي معين 
    success_url = reverse_lazy('project_list')

    
# دالة انشاء مهام 
class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    template_name = 'project/task_create_view.html'
    # لمنع المستخدم من استخدام غير بوست
    http_method_names = ['post']
    # تم استخدام هذه الدالة ليتم التوجيه الى نفس الصفحة بعد الاضافة 
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])

# دالة تعديل المهام 
# وتحمل عنصر واحد فقط 
class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']
    # يتم التوجيه الى نفس الصفحة بعد التعديل 
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


# دالة حذف الهام 
# لا تحتاج الا الى تحديد الموديل 
class TaskDeletView(DeleteView):
    model = models.Task
    # توجيه الصفحة الى الصفحة الرئيسية 
    # مع تمرير الاي دي الخاص بالمهمة 
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


