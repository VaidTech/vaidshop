from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'owner', 'gender', 'mobile_number')
	list_display_links = ('id', 'user')
	search_fields = ('user__username', 'id', 'mobile_number', 'gender')
	list_filter = ('gender',)
	readonly_fields = ('created_at', 'updated_at')
	
	class Meta:
		model = Employee 

admin.site.register(Employee, EmployeeAdmin)
