from django.core.exceptions import PermissionDenied
from functools import wraps

from .models import Shop 
from orders.models import Order 
from employees.models import Employee 


def shop_owner_entry_is_author(function):
    def wrap(request, *args, **kwargs):
        shop_instance = Shop.objects.get(id=kwargs['id'])
        if shop_instance.owner.user == request.user:
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


def order_user_entry_is_author(function):
    def wrap(request, *args, **kwargs):
        order_instance = Order.objects.get(id=kwargs['id'])
        if order_instance.user == request.user:
        	return function(request, *args, **kwargs)
        else:
        	return PermissionDenied
 
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
