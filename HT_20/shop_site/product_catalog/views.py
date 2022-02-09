from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Product, Category


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product


class CategoryDetailView(generic.DetailView):
    model = Category


def index(request, pk=None):
    num_product = Product.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    product_lst = Product.objects.all()
    category_lst = Category.objects.all()
    return render(request, 'product_catalog/index.html', context={
        'num_product': num_product,
        'num_visits': num_visits,
        'lst': product_lst,
        'lst_cat': category_lst
    })


def cat(request, pk=None):
    product_lst = Product.objects.all()
    category_lst = Category.objects.all()
    return render(request, 'product_catalog/category_detail.html', context={
        'lst': product_lst,
        'lst_cat': category_lst
    })

