from django import forms 
from employees.models import Employee
from accounts.models import User
from core.custom.others.permissions_data import employee_permission_qs 


class EmployeePermissionForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('user_permissions',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['user_permissions'].queryset = employee_permission_qs
		self.fields['user_permissions'].label_from_instance = lambda obj: "%s" % obj.natural_key()[0]