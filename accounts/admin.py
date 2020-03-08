from django.contrib import admin
from .models import User 


class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'is_owner')
	list_display_links = ('id', 'username')
	list_filter = ('is_owner', 'is_active')
	search_fields = ('email', 'username', 'id')
	
admin.site.register(User, UserAdmin)