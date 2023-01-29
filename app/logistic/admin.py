from django.contrib import admin

from logistic.models import StockProduct, Stock, Product


class OrderPositionInline(admin.TabularInline):
    model = StockProduct
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', ]
    # list_filter = ['category']


@admin.register(Stock)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    inlines = [OrderPositionInline, ]
