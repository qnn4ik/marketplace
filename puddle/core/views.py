from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import Count

from core.forms import SignUpUserForm, LoginUserForm
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all().annotate(total=Count('items'))

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })


def contact(request):
    return render(request, 'core/contact.html')


class SignUpUser(CreateView):
    """User registration"""
    form_class = SignUpUserForm
    template_name = 'core/sign_up.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('/login/')


class LoginUser(LoginView):
    """Login user"""
    form_class = LoginUserForm
    template_name = 'core/login.html'
    success_url = 'index/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def logout_user(request):
    logout(request)
    return redirect('/')
