from django.urls import path, include
from rest_framework import routers

from .views import ProductViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
