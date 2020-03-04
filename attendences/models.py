from django.db import models

from employees.models import Employee


class Attendence(models.Model): 
	employee 	= models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True) 
	date 		= models.DateField()
	entry_time = models.TimeField()
	exit_time = models.TimeField(blank=True, null=True, help_text="When you get home from work, fill out this field")
	is_approved = models.BooleanField("approval status", default=True)
	updated_at	= models.DateTimeField(auto_now=True)
	created_at	= models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return str(f"{self.employee} presented at {self.date}")




