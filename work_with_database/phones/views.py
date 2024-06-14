from pprint import pprint

from django.shortcuts import render
from django.urls import reverse

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if not sort:
        sort = 'name'
    else:
        if sort == 'min_price':
            sort = 'price'
        elif sort == 'max_price':
            sort = '-price'
    phones = Phone.objects.all().order_by(sort)
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    queryset = Phone.objects.get(slug=slug)
    sort = request.GET.get('sort')
    if request.GET.get('sort'):
        queryset.order_by(*sort.split(','))
    context = {
        'phone': queryset,
    }

    return render(request, template, context)
