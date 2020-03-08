from django.core.exceptions import PermissionDenied
from functools import wraps
from shops.models import Shop 
from orders.models import Order 
from employees.models import Employee 
from owners.models import Owner
from attendences.models import Attendence 


def shop_creator_entry_is_author(function):
    def wrap(request, *args, **kwargs):
        shop_instance = Shop.objects.get(id=kwargs['id'])
        user = request.user 
        if shop_instance.owner.user == user or shop_instance.creator == user:
        	return function(request, *args, **kwargs)
        else:
        	return PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def employee_owner_entry_is_author(function):
    def wrap(request, *args, **kwargs):
        employee_instance = Employee.objects.get(id=kwargs['id'])
        if employee_instance.owner.user == request.user:
        	return function(request, *args, **kwargs)
        else:
        	return PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def order_creator_entry_is_author(function):
    def wrap(request, *args, **kwargs):
        order_instance = Order.objects.get(id=kwargs['id'])
        user = request.user
        if user.is_owner:
            owner = Owner.objects.get(user=user)
        else:
            employee = user.employee 
            owner = employee.owner 
        if order_instance.creator == user or order_instance.owner.user == user:
        	return function(request, *args, **kwargs)
        else:
        	return PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def attendence_employee_entry_is_author(function):
    def wrap(request, *args, **kwargs):
        attendence_instance = Attendence.objects.get(id=kwargs['id'])
        user = request.user
        if attendence_instance.employee.user == user or attendence_instance.employee.owner.user == user:
            return function(request, *args, **kwargs)
        else:
            return PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap