from django.urls import path

from orders.views import Order_Create_View

app_name = 'orders'

urlpatterns = [
    path('create', Order_Create_View.as_view(), name='create'),
]

