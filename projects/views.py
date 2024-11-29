from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView  ,UpdateView, DeleteView
from django.urls import reverse_lazy ,reverse
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# لعرض المشاريع الموجود 
class Project_View(LoginRequiredMixin,ListView):
    model = models.Project
    template_name = 'project/list_view.html'
    paginate_by = 6
     

    def get_queryset(self) :
        # جلب البيانات من موديل 
        query_set= super().get_queryset()
        # انشاء اقموس فارغ 
        where= {}
        # تخزين المدخلات في فورم البحث في متغير 
        #تم استيراد البيانت من فورم بواسطة كيت
        q= self.request.GET.get('q',None)
        # في حال كانت لبيانات مطابقة للمتغير الذي ادخله المستخدم يتم 
        # اي هنا تم تخوين الشرط 
        if q : where['title__icontains'] =q
        # تطبيق الشرك بواسطة دالة الفلتر 
        return query_set.filter(**where)


# دالة انشاء المشاريع 
class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = models.Project
    form_class = forms.Project_Create_View
    template_name = 'project/create_view.html'
    # متغير ثابت 
    # سيستخدم عند عدم الحاجة الى استخدام اي دي المشروع 
    success_url = reverse_lazy('project_list')


#دالة تعديل المشاريع 
class Projectupdateview(LoginRequiredMixin,UpdateView):
    model = models.Project
    form_class = forms.Project_Update_View
    template_name = 'project/update_view.html'
    # دالة التوجيه 
    #تستخدم عند الحاجة الى الحصول ال ايدي  مشروع معين 
    # حيق يتم التوجيه الى الصفحة نفسها  بعد التتعديل 
    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])
    
# دالة حذف المشاريع 
class ProjectDeletView(LoginRequiredMixin,DeleteView):
    model = models.Project
    template_name = 'project/delete_view.html'
    # لم يتم استخدام الدالة لاننها هنا لم نحتج الى الحصول على اي دي معين 
    success_url = reverse_lazy('project_list')

    
# دالة انشاء مهام 
class TaskCreateView(LoginRequiredMixin,CreateView):
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
class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Task
    fields = ['is_completed']
    http_method_names = ['post']
    # يتم التوجيه الى نفس الصفحة بعد التعديل 
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


# دالة حذف الهام 
# لا تحتاج الا الى تحديد الموديل 
class TaskDeletView(LoginRequiredMixin,DeleteView):
    model = models.Task
    # توجيه الصفحة الى الصفحة الرئيسية 
    # مع تمرير الاي دي الخاص بالمهمة 
    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])
