from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from .forms import NewItemForm, EditItemForm
from .models import Item, Category


def items(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    try:
        cat_id = int(request.GET.get('category', 0))
    except ValueError:
        cat_id = 0

    if cat_id:
        items = items.filter(category_id=cat_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'cat_id': cat_id,
    })


class ItemDetail(DetailView):
    model = Item
    template_name = 'item/detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_items = Item.objects.filter(category=self.object.category, is_sold=False).exclude(pk=self.object.pk)[0:3]
        context['related_items'] = related_items

        return context


class CreateItem(LoginRequiredMixin, CreateView):
    """Create a new item"""
    model = Item
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


class EditItem(LoginRequiredMixin, UpdateView):
    """Edit the item content"""
    model = Item
    form_class = EditItemForm
    template_name = 'item/form.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit item'
        return context

    def form_valid(self, form):
        self.object.save()
        return redirect('item:detail', pk=self.object.id)

    def get_queryset(self):  # returns a query only to a certain user
        queryset = super(EditItem, self).get_queryset()
        queryset = queryset.filter(created_by=self.request.user)
        return queryset


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
