from django import forms 
from datetime import datetime

from .models import Attendence
from employees.models import Employee 


class AttendenceForm(forms.ModelForm):
	date = forms.DateField(
	        widget=forms.DateInput(format='%m/%d/%Y'),
	        input_formats=('%m/%d/%Y', )
	    )
	class Meta:
		model = Attendence
		fields = ('employee', 'date', 'entry_time', 'exit_time')

	def __init__(self, user, *args, **kwargs):
		super().__init__(*args, **kwargs)
		employee = None
		if user.is_owner:
			owner = user.owner 
			employee = Employee.objects.filter(owner=owner)
		self.fields['employee'].queryset = employee



	


