from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from orders.forms import Order_Form
from common.views import Title_Mixin


class Order_Create_View(Title_Mixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = Order_Form
    success_url = reverse_lazy('orders:create')
    title = 'Store - Оформление заказа'
