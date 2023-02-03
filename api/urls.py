from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet, BasketViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'baskets', BasketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
