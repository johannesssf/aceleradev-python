from django.shortcuts import render, redirect

from products.models import Product
from products.forms import ProductModelForm


def list_products(request):
    prods = Product.objects.all()
    context = {
        'products': prods,
        'products_empty': [],
    }

    return render(request, 'products/list.html', context=context)


def create_produtct(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductModelForm()

    context = {
        'form': form
    }
    return render(request, 'products/create.html', context=context)
