from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .forms import NewItemForm
from .models import Item


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


class NewItem(LoginRequiredMixin, CreateView):
    form_class = NewItemForm
    template_name = 'item/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New item'
        return context

    def form_valid(self, form):
        item = form.save(commit=False)
        item.created_by = self.request.user
        item.save()
        return redirect('item:detail', pk=item.id)
