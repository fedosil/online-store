from django.urls import path

from orders.views import Order_Create_View, Success_View, Cancel_View, OrderList_View, OrderDetail_View

app_name = 'orders'

urlpatterns = [
    path('create/', Order_Create_View.as_view(), name='create'),
    path('success/', Success_View.as_view(), name='success'),
    path('cancel/', Cancel_View.as_view(), name='cancel'),
    path('list/', OrderList_View.as_view(), name='list'),
    path('detail/<int:pk>/', OrderDetail_View.as_view(), name='detail'),
]

