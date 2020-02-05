from django.shortcuts import render, redirect 
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import UserForm, OwnerRegisterForm, LoginForm
from owners.models import Owner

User = get_user_model()

def owner_register_view(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        o_r_form = OwnerRegisterForm(request.POST, request.FILES)
        if form.is_valid() and o_r_form.is_valid():
            user = form.save()
            instance = o_r_form.save(commit=False)
            instance.user = user 
            instance.save()
            return redirect('accounts:login')
    else:
        form = UserForm()
        o_r_form = OwnerRegisterForm()
    context = {
        'form': form,
        'o_r_form': o_r_form
    }
    return render(request, 'accounts/owner-register.html', context)


def login_view(request):
    is_login = False
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user) 
                is_login = True            
    else:
        form = LoginForm()
    context = {
        'login_form': form
    }
    if request.is_ajax():
        json_data={
            'is_login': is_login
        }
        return JsonResponse(json_data)
    return render(request, 'accounts/login.html', context)


@login_required(login_url="/accounts/login/")
def dashboard_view(request):
    obj = User.objects.get(id=request.user.id)
    is_owner = Owner.objects.filter(user=obj).exists()
    context = {}
    if is_owner:
        return render(request, 'owners/owner_dashboard.html', context)
    return render(request, 'employees/employee_dashboard.html', context)
    



