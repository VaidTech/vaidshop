from django.contrib import admin
from .models import Shop


class ShopAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'owner', 'creator')
	list_display_links = ('id', 'name')
	search_fields = ('id', 'name', 'owner', 'creator')
	readonly_fields = ('created_at', 'updated_at')

	class Meta:
		model = Shop

admin.site.register(Shop, ShopAdmin)