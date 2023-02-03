from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductListApiView

app_name = 'api'

urlpatterns = [
    path('product-list/', ProductListApiView.as_view(), name='products_list'),
]

