from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .forms import AttendenceForm 
from owners.models import Owner
from .models import Attendence
from employees.models import Employee
from core.custom.others.choices import months, years
from core.custom.decorator.decorators import attendence_employee_entry_is_author


@login_required
@permission_required('attendences.add_attendence', raise_exception=True)
def attendence_add_view(request):
	if request.method == 'POST':
		attendence_form = AttendenceForm(request.user, request.POST)
		if attendence_form.is_valid():
			attendence_instance = attendence_form.save(commit=False)
			if not request.user.is_owner:
				user = request.user 
				employee = user.employee
				attendence_instance.employee = employee
			attendence_instance.save()
			messages.success(request, 'Success your attendence is added.')
			return redirect("attendences:attendence-list")
	else:
		attendence_form = AttendenceForm(request.user)
	context = {
		'attendence_form': attendence_form
	}
	return render(request, 'attendences/attendence-create.html', context)


@login_required
@attendence_employee_entry_is_author
@permission_required('attendences.change_attendence', raise_exception=True)
def attendence_edit_view(request, id):
	attendence_object = Attendence.objects.get(id=id)
	if request.method == 'POST':
		attendence_form = AttendenceForm(request.user, request.POST, instance=attendence_object)
		if attendence_form.is_valid():
			attendence_instance = attendence_form.save(commit=False)
			if not request.user.is_owner:
				user = request.user 
				employee = user.employee
				attendence_instance.employee = employee
			attendence_instance.save()
			messages.success(request, 'Success your attendence is updated.')
			return redirect("attendences:attendence-list")
	else:
		attendence_form = AttendenceForm(request.user, instance=attendence_object)
	context = {
		'attendence_form': attendence_form,
		'attendence_object': attendence_object
	}
	return render(request, 'attendences/attendence-create.html', context)


@login_required
@permission_required('attendences.view_attendence', raise_exception=True)
def attendence_list(request):
	user = request.user
	attendence_qs = None
	employee_qs = None
	employee_attendence = None
	# searching when owner loged in
	if user.is_owner:
		owner = Owner.objects.get(user=user)
		employee_qs = Employee.objects.filter(owner=owner)
		attendence_qs = Attendence.objects.filter(employee__owner=owner)
		if "employee_name" in request.GET:
			employee_name = request.GET.get('employee_name')
			if employee_name:
				attendence_qs = attendence_qs.filter(employee__user__username__iexact=employee_name)
		if "month" in request.GET:
			month = request.GET.get('month')
			if month:
				attendence_qs = attendence_qs.filter(date__month=month)
		if "year" in request.GET:
			year = request.GET.get('year')
			if year:
				attendence_qs = attendence_qs.filter(date__year=year)
	# searching when employee loged in
	else:
		employee = user.employee
		employee_attendence = Attendence.objects.filter(employee=employee)
		if "month" in request.GET:
			month = request.GET.get('month')
			if month:
				employee_attendence = employee_attendence.filter(date__month=month)
		if "year" in request.GET:
			year = request.GET.get('year')
			if year:
				employee_attendence = employee_attendence.filter(date__year=year)
	context = {
		'attendence_qs': attendence_qs,
		'employee_qs': employee_qs,
		'employee_attendence': employee_attendence,
		'months': months,
		'years': years
	}
	return render(request, 'attendences/attendence-list.html', context)


@login_required
@permission_required('attendences.view_attendence', raise_exception=True)
def attendence_list_detail(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	employee_attendence = Attendence.objects.filter(employee=employee)
	context = {
		'employee_attendence': employee_attendence
	}
	return render(request, 'attendences/attendence-list-detail.html', context)


@login_required
@attendence_employee_entry_is_author
@permission_required('attendences.delete_attendence', raise_exception=True)
def attendence_delete_view(request, id):
	data = dict()
	attendence_object = get_object_or_404(Attendence, id=id)
	if request.method == 'POST':
		if attendence_object:
			attendence_object.delete()
			data['is_success'] = True 
			return JsonResponse(data)
	context = {
		'attendence_object': attendence_object
	}
	if request.is_ajax():
		data['html_form'] = render_to_string('attendences/attendence-delete.html', context, request=request)
		return JsonResponse(data)
	return render(request, 'attendences/attendence-delete.html', context)


@login_required
@permission_required('attendences.view_attendence', raise_exception=True)
def attendence_chart_view(request):
	data = []
	labels = []
	user = request.user
	year = request.GET.get('chart_year', 2020)
	print(year)
	if user.is_owner:
		owner = user.owner 
		employee_qs = Employee.objects.filter(owner=owner)
		attendence_qs = Attendence.objects.all()
		for employee in employee_qs:
			labels.append(employee.user.username)
			attendences = Attendence.objects.filter(employee=employee, date__year=year)
			months = []
			for i in range(1,13):
				months.append(attendences.filter(date__month=i).count())
			data.append(months)
	else:
		pass
	return JsonResponse({'data':data, 'labels': labels})


def is_owner(user):
	return user.is_owner 

@login_required
@user_passes_test(is_owner)
@permission_required('attendences.view_attendence', raise_exception=True)
def attendence_annual_view(request):
	context = {
		'years': years
	}
	return render(request, 'attendences/annual-attendence.html', context)
