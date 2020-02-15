from django.shortcuts import render, redirect 
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse 
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import EmployeeForm
from .models import Employee
from accounts.forms import UserForm, UserUpdateForm
from owners.models import Owner

User = get_user_model()


def employee_create_view(request):
    error_dict = {}
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST,request.FILES)
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


def employee_update_view(request, id):  
    data = dict()
    employee_instance = Employee.objects.get(id=id)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, initial={'username': employee_instance.user.username, 'email': employee_instance.user.email})
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee_instance)
        if employee_form.is_valid() and user_form.is_valid():
            username = user_form.cleaned_data.get("username")
            email = user_form.cleaned_data.get("email")
            employee_qs = Employee.objects.filter(user__username=username).exclude(id=id).exists()
            if employee_qs:
                data['username_error'] = {"error": "Username is already taken!"}
                # raise ValidationError("Username is already taken!")
                return JsonResponse(data)
            instance_user = employee_instance.user
            instance_user.username = username
            if email:
                instance_user.email = email 
            instance_user.save()
            employee_form.save()
            # data['employee_list'] = render_to_string('employees/employee-list.html', {
            #     'instance': employee_instance
            # })
            return redirect("/employee/list/")
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


def employee_delete_view(request, id):
    data = dict()
    is_delete = request.GET.get('delete')
    print(is_delete)
    try:
        employee_instance = Employee.objects.get(id=id)
    except:
        data['errors'] = 'does not exists'
        return redirect("/")
    if employee_instance and is_delete:
        employee_instance.delete()
        return redirect("employees:list")
    else:
        # return reverse("employees:detail", kwargs={'id': id})
        pass
    context = {
        'object': employee_instance
    }
    if request.is_ajax():
        data['html_form'] = render_to_string('employees/employee-delete.html', context, request=request)
        return JsonResponse(data)
    return render(request, 'employees/employee-delete.html', context)


def employee_list_view(request):
    form = UserForm()
    employee_form = EmployeeForm()
    owner = Owner.objects.get(user=request.user)
    employee_qs = owner.employees.all()

    page_number = request.GET.get('page')
    paginator = Paginator(employee_qs, 10)
    page_obj = paginator.get_page(page_number) 
    context = {
        'form': form,
        'employee_form': employee_form,
        'page_obj': page_obj

    }
    return render(request, 'employees/employee-list.html', context)



