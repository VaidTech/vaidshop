from django import forms 
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from employees.models import Employee
from accounts.models import User 


employee_permission_qs = Permission.objects.exclude(
		content_type__app_label='auth'
		).exclude(
		content_type__app_label='accounts'
		).exclude(
		content_type__app_label='sessions'
		).exclude(
		content_type__app_label='core'
		).exclude(
		content_type__app_label='employees'
		).exclude(
		content_type__app_label='owners'
		).exclude(
		content_type__app_label='admin'
		).exclude(
		content_type__app_label='contenttypes'
		).exclude(
		content_type__model='customer'
		).exclude(
		content_type__model='orderproduct'
		).exclude(
		content_type__model='stock'
	)

class EmployeePermissionForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('user_permissions',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['user_permissions'].queryset = employee_permission_qs
		self.fields['user_permissions'].label_from_instance = lambda obj: "%s" % obj.natural_key()[0]