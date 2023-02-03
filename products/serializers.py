from rest_framework import serializers, fields

from .models import Product, Category, Basket


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'image', 'category']

class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    sum = fields.FloatField()
    total_sum = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    class Meta:
        model = Basket
        fields = ('id', 'product', 'quantity', 'sum', 'total_sum', 'total_quantity', 'created_at',)
        read_only_fields = ('created_at',)

    def get_total_sum(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user.id).total_quantity()