from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import List


class CustomLoginView(LoginView):
    template_name = 'list/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('items')


class RegisterPage(FormView):
    template_name = 'list/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('items')
        return super(RegisterPage, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = List
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = context['items'].filter(user=self.request.user)
        context['count'] = context['items'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['items'] = context['items'].filter(
                title__startswith=search_input)
        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = List
    context_object_name = 'item'
    template_name = 'list/list.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('items')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = List
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('items')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = List
    context_object_name = 'item'
    success_url = reverse_lazy('items')