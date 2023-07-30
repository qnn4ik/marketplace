from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from core.forms import SignUpUserForm
from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items
    })


def contact(request):
    return render(request, 'core/contact.html')


class SignUp(CreateView):
    """User registration"""
    form_class = SignUpUserForm
    template_name = 'core/sign_up.html'
    # success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')
