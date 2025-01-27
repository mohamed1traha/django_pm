from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from user.forms import UseRegisterForm, ProfileForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # إعادة التوجيه إلى صفحة تسجيل الدخول


class RegisterView(FormView):
    form_class=UseRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def edit_profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST,instance = request.user) 
        
        if form.is_valid():
            form.save()
            return redirect('profile')
        
        else:
            return render(request, 'profile.html',{
                'form': form
            })
    else:
        form = ProfileForm(instance=request.user)  # تهيئة النموذج بالبيانات الحالية للمستخدم
    
    return render(request, 'profile.html', {'form': form})  # عرض النموذج مع البيانات الحالية
    
