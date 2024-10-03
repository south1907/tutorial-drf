from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_sale_price = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'my_sale_price'
        ]

    def get_my_sale_price(self, obj):
        print(obj.id)
        return obj.sale_price