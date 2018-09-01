from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Brand
from django.utils import timezone
from .forms import BrandForm

@login_required
def list_brands(request):
    brands = Brand.objects.all()
    return render(request, 'brands/list_brands.html', {'brands': brands})

@login_required
def create_brand(request):
    form = BrandForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_brands')

    return render(request, 'brands/brand_form.html', {'form': form})


@login_required
def update_brand(request, id):
    brands = Brand.objects.get(id = id)

    form = BrandForm(request.POST or None, instance = brands)
    if form.is_valid():
        form.save()
        return redirect('list_brands')

    return render(request, 'brands/brand_form.html', {'form': form, 'brands': brands})
