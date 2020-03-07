from django.contrib import admin
from .models import Owner


class OwnerAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')
	list_display_links = ('id', 'user')
	search_fields = ('id', 'user__username')

	class Meta:
		model = Owner

admin.site.register(Owner, OwnerAdmin)
