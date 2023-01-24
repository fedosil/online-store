import stripe
from http import HTTPStatus

from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from orders.forms import Order_Form
from common.views import Title_Mixin

stripe.api_key = settings.STRIPE_SECRET_KEY

class Success_View(Title_Mixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Store - Спасибо за заказ!'

class Cancel_View(TemplateView):
    template_name = 'orders/cancel.html'

class Order_Create_View(Title_Mixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = Order_Form
    success_url = reverse_lazy('orders:create')
    title = 'Store - Оформление заказа'

    def post(self, request, *args, **kwargs):
        super(Order_Create_View, self).post(request, *args, **kwargs)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1MSGgdKJN9Z2V10jGV18oo1Y',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:cancel')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(Order_Create_View, self).form_valid(form)


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body

    # For now, you only need to print out the webhook payload so you can see
    # the structure.
    print(payload)

    return HttpResponse(status=200)
