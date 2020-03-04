from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from shops.models import Shop 
from accounts.models import User 
from .forms import EmployeePermissionForm
from owners.models import Owner




def user_gains_perms(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	permission_instance = Permission.objects.filter(user=user)
	if request.method == 'POST':
		employee_permission_form = EmployeePermissionForm(request.POST, instance=user)
		if employee_permission_form.is_valid():
		    user.user_permissions.set(employee_permission_form.cleaned_data.get('user_permissions'))
		    return redirect("permissions:permission-list")
	else:
		employee_permission_form = EmployeePermissionForm(instance=user)
	context = {
		'employee_permission_form': employee_permission_form,
		'employee_user_id': user.id
	}
	return render(request, 'permissions/permission.html', context)


def permission_list(request):
	owner = Owner.objects.get(user=request.user)
	context = {
		'owner': owner
	}
	return render(request, 'permissions/permission-list.html', context)
