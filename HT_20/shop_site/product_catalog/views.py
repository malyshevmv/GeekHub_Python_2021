from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Product, Category


def index(request):
    num_product = Product.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'product_catalog/index.html', context={
        'num_product': num_product,
        'num_visits': num_visits
    })


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product

