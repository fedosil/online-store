from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import *

app_name = 'products'

urlpatterns = [
    path('', Products_view.as_view(), name='products'),
    path('category/<int:category_id>/', Products_view.as_view(), name='category'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:pk>/', basket_remove, name='basket_remove'),
]

