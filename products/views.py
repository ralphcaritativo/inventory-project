from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone
from .forms import ProductForm

@login_required
def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_products.html', {'products': products})

@login_required
def create_product(request):
    form = ProductForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('list_products')
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def update_product(request, id):
    products = Product.objects.get(id = id)

    form = ProductForm(request.POST or None, request.FILES or None, instance = products)
    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products/product_form.html', {'form': form, 'products': products})
