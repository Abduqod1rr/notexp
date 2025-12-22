from django.shortcuts import render
from django.views.generic import CreateView ,DeleteView,ListView ,UpdateView
from forms import UserForm
# Create your views here.


class RegisterUser(CreateView):
    form_class=UserForm
    template_name=''
    success_url=''
    
