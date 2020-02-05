from django.shortcuts import render, redirect 
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.contrib import messages


from .forms import EmployeeForm
from accounts.forms import UserForm
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
    


def employee_list_view(request):
    form = UserForm()
    employee_form = EmployeeForm()
    owner = Owner.objects.get(user=request.user)
    context = {
        'form': form,
        'employee_form': employee_form,
        'owner': owner
    }
    return render(request, 'employees/employee-list.html', context)



