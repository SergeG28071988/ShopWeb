from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):
    products = Product.objects.order_by('-id')
    context = {'title': 'Главная страница сайта', 'products': products}
    return render(request, 'base/index.html', context)


def add_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма была не верной"
    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'base/add_product.html', context)


def about(request):
    return render(request, 'base/about.html')
