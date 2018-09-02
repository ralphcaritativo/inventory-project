from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category
from django.utils import timezone
from .forms import CategoryForm

@login_required
def list_category(request):
    categories = Category.objects.all()
    return render(request, 'categories/list_category.html', {'categories': categories})

@login_required
def create_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_category')

    return render(request, 'categories/category_form.html', {'form': form})

@login_required
def update_category(request, id):
    categories = Category.objects.get(id = id)

    form = CategoryForm(request.POST or None, instance = categories)
    if form.is_valid():
        form.save()
        return redirect('list_category')

    return render(request, 'categories/category_form.html', {'form': form, 'categories': categories})
