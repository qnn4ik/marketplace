from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from item.models import Item


class DashboardHome(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'dashboard/index.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My items'
        return context

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user)
