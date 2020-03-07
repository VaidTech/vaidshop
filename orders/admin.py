from django.contrib import admin
from .models import Order, Customer, OrderProduct


class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'creator', 'owner', 'customer', 'active')
	list_display_links = ('id', 'creator')
	readonly_fields = ('created_at',)
	search_fields = ('id', 'creator__username', 'owner__user__username', 'customer__name')
	class Meta:
		model = Order

admin.site.register(Order, OrderAdmin)


class CustomerAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'phone_number', 'address')
	list_display_links = ('id', 'name')
	search_fields = ('id', 'name', 'phone_number')
	class Meta:
		model = Customer

admin.site.register(Customer, CustomerAdmin)


class OrderProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'order', 'product', 'quantity')
	list_display_links = ('id', 'product')
	search_fields = ('id', 'order__id', 'quantity')
	readonly_fields = ('created_at',)
	class Meta:
		model = OrderProduct

admin.site.register(OrderProduct, OrderProductAdmin)
