from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

class Order_Create_View(TemplateView):
    template_name = 'orders/order-create.html'
