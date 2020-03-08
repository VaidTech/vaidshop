from django.contrib import admin
from .models import Attendence


class AttendenceAdmin(admin.ModelAdmin):
	list_display = ('id', 'employee', 'date', 'entry_time', 'exit_time', 'is_approved')
	list_display_links = ('id', 'employee')
	readonly_fields = ('created_at', 'updated_at')

	class Meta:
		model = Attendence

admin.site.register(Attendence, AttendenceAdmin)
