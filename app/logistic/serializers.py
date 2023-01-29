from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ['title', 'description']
        search_fields = ['title', 'products__title', 'products__description']
        ordering_fields = ['title']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)


    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = '__all__'


    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        for item in positions:
            StockProduct.objects.create(stock=stock, **item)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        for element in positions:
            obj, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=element['product'],
                defaults={'stock': stock, 'product': element['product'], 'quantity': element['quantity'], 'price': element['price']}
            )
        return stock