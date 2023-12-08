from django.shortcuts import render
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignupView(TemplateView):
    form_class= UserCreationForm
    template_name = 'home/register.html'
    success_url = '/notes/list'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return render(request, self.template_name, {'form' : form})

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