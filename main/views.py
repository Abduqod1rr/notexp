from django.shortcuts import render
from django.views.generic import ListView,DeleteView ,UpdateView ,CreateView
from .models import ToDos ,EXPS
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginRequiredMixin,ListView):
    model=ToDos
    template_name='home.html'
    context_object_name='todos'

    def get_queryset(self):
        # Only show the logged-in user's todos
        return ToDos.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add user's current XP to context
        exps, created = EXPS.objects.get_or_create(owner=self.request.user)
        context['current_xp'] = exps.amount
        return context