from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout_view(request):
    logout(request)
    return redirect('login')  # إعادة التوجيه إلى صفحة تسجيل الدخول
