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
    if request.method == "POST":
        if request.POST['name'] and request.POST['description'] and request.POST['sku'] and request.POST['price'] and request.POST['quantity'] and request.FILES['image']:
            product = Product()
            product.name = request.POST['name']
            product.description = request.POST['description']
            product.sku = request.POST['sku']
            product.price = request.POST['price']
            product.quantity = request.POST['quantity']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.save()
            return redirect('list_products')
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'products/create.html')

@login_required
def update_product(request, id):
    if request.method == "POST":
        if request.POST['name'] and request.POST['description'] and request.POST['sku'] and request.POST['price'] and request.POST['quantity'] and request.FILES['image']:
            product = Product.objects.get(id = id)
            product.name = request.POST['name']
            product.description = request.POST['description']
            product.sku = request.POST['sku']
            product.price = request.POST['price']
            product.quantity = request.POST['quantity']
            product.image = request.FILES['image']
            product.save()
            return redirect('list_products')
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required.'})
    else:
        return render(request, 'products/update.html')
