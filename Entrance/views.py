from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from  .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):#「LoginRequiredMixin → TemplateView」この順番で記述しないとログイン必須機能が表れないので注意！！
    template_name = 'home.html'
    login_url = '/login/'
    
class Login(LoginView):
    template_name = 'login.html'
    form_class = LoginForm