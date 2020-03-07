from django.contrib import admin
from .models import StockType


class StockTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	list_display_links = ('id', 'name')
	readonly_fields = ('created_at', 'updated_at')
	class Meta:
		model = StockType

admin.site.register(StockType, StockTypeAdmin)
