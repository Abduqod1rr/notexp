from django.shortcuts import render 
from django.views.generic import CreateView ,DeleteView,ListView ,UpdateView
from .forms import UserForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView ,LogoutView
from django.urls import reverse_lazy
# Create your views here.


class RegisterUser(CreateView):
    form_class=UserForm
    template_name='register.html'
    success_url=reverse_lazy('login')

class UserLogin(LoginView):
    template_name='login.html'
    success_url=reverse_lazy('home')
   
    
