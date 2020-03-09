from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'is_owner')
	list_display_links = ('id', 'username')
	list_filter = ('is_owner', 'is_active')
	search_fields = ('email', 'username', 'id')
	
admin.site.register(User, UserAdmin)