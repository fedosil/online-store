from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from orders.views import stripe_webhook_view
from products.views import Index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index_view.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('accounts/', include('allauth.urls')),
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),
    path('api/', include('api.urls', namespace='api')),
    path('api-token-auth/', views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
