from django.contrib import admin

from .models import Basket, Category, Product

admin.site.register(Category)


@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    fields = ['name', 'description', ('price', 'quantity'), 'image', 'stripe_price_id', 'category']
    readonly_fields = ['description']


class Bascet_admin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_at']
    readonly_fields = ['created_at']
    extra = 0

