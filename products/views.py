from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.cache import cache

from common.views import Title_Mixin
from users.models import User

from .models import Basket, Category, Product


class Products_view(Title_Mixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    # allow_empty = False  # 404 для неправильной ссылки
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = super(Products_view, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(Products_view, self).get_context_data()
        categories = cache.get_or_set('categories', Category.objects.all(), 10)
        context['categories'] = categories
        return context

class Index_view(Title_Mixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'

    def get_context_data(self, **kwargs):
        context = super(Index_view, self).get_context_data()
        return context


# def products(request, category_id=None, page=1):
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     per_page = 1
#     paginator = Paginator(products, per_page=per_page)
#     products_paginator = paginator.get_page(page)
#     context = {
#         'title': 'Store - каталог',
#         'products': products_paginator,
#         'categories': Category.objects.all()
#     }
#     return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(pk=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, pk):
    basket = Basket.objects.get(pk=pk)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
