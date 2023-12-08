from django.shortcuts import render
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'name': 'Django', 'current_time': datetime.now()}
    
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'