# permissions qs 
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

owner_permission_qs = Permission.objects.exclude(
    content_type__app_label='auth'
    ).exclude(
    content_type__app_label='accounts'
    ).exclude(
    content_type__app_label='sessions'
    ).exclude(
    content_type__app_label='core'
    ).exclude(
    content_type__app_label='owners'
    ).exclude(
    content_type__app_label='admin'
    ).exclude(
    content_type__app_label='contenttypes'
    ).exclude(
    content_type__model='stock')

employee_permission_qs = owner_permission_qs.exclude(content_type__model='customer').exclude(
	content_type__model='orderproduct')
