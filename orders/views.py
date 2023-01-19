from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from orders.models import Order
from orders.forms import Order_Form


class Order_Create_View(CreateView):
    template_name = 'orders/order-create.html'
    # model = Order
    form_class = Order_Form
