from django.shortcuts import render, redirect 
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse 
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from core.custom.decorator.decorators import employee_owner_entry_is_author
from .forms import EmployeeForm
from .models import Employee
from accounts.forms import UserForm, UserUpdateForm
from owners.models import Owner
from accounts.models import User 


def user_is_owner(user):
    return user.is_owner

@login_required
@user_passes_test(user_is_owner)
@permission_required('employees.add_employee', raise_exception=True)
def employee_create_view(request):
    error_dict = {}
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        form = UserForm(request.POST)
        if employee_form.is_valid() and form.is_valid():
            user = form.save()
            instance = employee_form.save(commit=False)
            owner = Owner.objects.get(user=request.user)
            instance.owner = owner
            instance.user = user 
            instance.save()
            messages.success(request, 'Employee successfully registered.')
            return redirect("employees:list")
        else:
            error_dict= {'status':'form-invalid','form_errors':form.errors, 'emp_errors': employee_form.errors}
    else:
        employee_form = EmployeeForm()
        form = UserForm()
    context = {
        'employee_form': employee_form, 
        'form': form,
    }
    if request.is_ajax():
        json_data = {
            'error_dict': error_dict
        }
        return JsonResponse(json_data)
    return render(request, 'employees/create-employee.html', context)


@login_required
@user_passes_test(user_is_owner)
@employee_owner_entry_is_author
@permission_required('employees.change_employee', raise_exception=True)
def employee_update_view(request, id):  
    data = dict()
    employee_instance = Employee.objects.get(id=id)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, initial={'username': employee_instance.user.username, 'email': employee_instance.user.email})
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee_instance)
        if employee_form.is_valid() and user_form.is_valid():
            username = user_form.cleaned_data.get("username")
            email = user_form.cleaned_data.get("email")
            user_qs = User.objects.filter(username=username).exclude(id=employee_instance.user.id).exists()
            if user_qs:
                data['username_error'] = {"error": "Username is already taken!"}
                return JsonResponse(data)
            else:
                instance_user = employee_instance.user
                instance_user.username = username
                if email:
                    instance_user.email = email 
                instance_user.save()
            employee_form.save()
        else:
            data['errors'] = {'status': 'form-invalid', 'employee_user_errors': user_form.errors, 'employee_errors': employee_form.errors}
    else:
        user_form = UserUpdateForm(initial={'username': employee_instance.user.username, 'email': employee_instance.user.email})
        employee_form = EmployeeForm(instance=employee_instance)
    context = {
        'user_form': user_form,
        'employee_form': employee_form,
        'object': employee_instance
    }
    if request.is_ajax():
        data['html_form'] = render_to_string('employees/employee-form.html', context, request=request)
        return JsonResponse(data)
    return render(request, 'employees/employee-update.html', context)
 

@login_required
@user_passes_test(user_is_owner)
@employee_owner_entry_is_author
@permission_required('employees.delete_employee', raise_exception=True)
def employee_delete_view(request, id):
    data = dict()
    is_delete = request.GET.get('delete')
    try:
        employee_instance = Employee.objects.get(id=id)
    except:
        data['errors'] = 'does not exists'
        return redirect("/")
    if employee_instance and is_delete:
        employee_instance.delete()
        return redirect("employees:list")
    else:
        pass
    context = {
        'object': employee_instance
    }
    if request.is_ajax():
        data['html_form'] = render_to_string('employees/employee-delete.html', context, request=request)
        return JsonResponse(data)
    return render(request, 'employees/employee-delete.html', context)


@login_required
@permission_required('employees.view_employee', raise_exception=True)
def employee_list_view(request):
    page_obj = None
    form = UserForm()
    employee_form = EmployeeForm()
    try:
        owner = Owner.objects.get(user=request.user)
        employee_qs = owner.employees.all()
        page_number = request.GET.get('page')
        paginator = Paginator(employee_qs, 10)
        page_obj = paginator.get_page(page_number) 
    except:
        pass 
    context = {
        'form': form,
        'employee_form': employee_form,
        'page_obj': page_obj
    }
    return render(request, 'employees/employee-list.html', context)


@login_required
@permission_required('employees.view_employee', raise_exception=True)
def employee_detail_view(request, id):
    employee_object = Employee.objects.get(id=id)
    context = {
        'employee_object': employee_object 
    }
    return render(request, 'employees/employee-detail.html', context)
