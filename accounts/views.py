from django.shortcuts import render, redirect 
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import UserForm, OwnerRegisterForm, LoginForm
from owners.models import Owner
from accounts.models import User 
from core.custom.others.permissions_data import owner_permission_qs


def owner_register_view(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        owner_register_form = OwnerRegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and owner_register_form.is_valid():
            user_instance = user_form.save()
            instance = owner_register_form.save(commit=False)
            instance.user = user_instance
            instance.user.is_owner = True 
            instance.save()
            instance.user.save()
            user = instance.user 
            user.user_permissions.set(owner_permission_qs)
            messages.success(request, 'Successfully owner registered.')
            return redirect('accounts:login')
    else:
        user_form = UserForm()
        owner_register_form = OwnerRegisterForm()
    context = {
        'form': user_form,
        'o_r_form': owner_register_form
    }
    return render(request, 'accounts/owner-register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:dashboard")
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


@login_required()
def logout_view(request):
    logout(request)
    return redirect("accounts:login")


@login_required()
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html', {})
    

@login_required()
def profile_view(request):
    context = {}
    return render(request, 'accounts/profile.html', context)