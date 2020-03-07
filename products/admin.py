from django.contrib import admin
from .models import Product, Stock


class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'shop', 'price')
	list_display_links = ('id', 'title')
	search_fields = ('id', 'title', 'price')
	readonly_fields = ('created_at', 'updated_at')

	class Meta:
		model = Product

admin.site.register(Product, ProductAdmin)


class StockAdmin(admin.ModelAdmin):
	list_display = ('id', 'stock_type', 'stock_quantity')
	list_display_links = ('id', 'stock_type')
	search_fields = ('id', 'stock_type', 'stock_quantity')
	readonly_fields = ('created_at', 'updated_at')

	class Meta:
		model = Stock

admin.site.register(Stock, StockAdmin)