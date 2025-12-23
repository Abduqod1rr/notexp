from django.shortcuts import render ,get_object_or_404 ,redirect
from django.views.generic import ListView,DeleteView ,UpdateView ,CreateView
from .models import ToDos ,EXPS
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
    
class addToDo(LoginRequiredMixin,CreateView):
    model = ToDos
    template_name='create.html'
    fields=['title','about','exp']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
    
class deleteToDo(LoginRequiredMixin,DeleteView):
    model = ToDos
    success_url = reverse_lazy('home')

    def test_func(self):
        obj=self.get_object()
        return obj.owner==self.request.user
    
@login_required
def toggle_todo_status(request,pk):
    todo = get_object_or_404(ToDos,pk= pk,owner=request.user)

    if todo.status=='waiting':
        todo.status = 'fineshed'

        exps , created = EXPS.objects.get_or_create(owner=request.user)
        exps.amount += todo.exp

        exps.save()
    else:
        todo.status='waiting'

        exps = EXPS.objects.get(owner=request.user)
        exps.amount -= todo.exp

        exps.save()

    todo.save()
    return redirect('home')