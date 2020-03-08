from django.urls import path  
from .views import user_gains_perms, permission_list

app_name = 'permissions'


urlpatterns = [
	path('permission/<int:user_id>/', user_gains_perms, name='employee-permission'),
	path('permission/view/', permission_list, name='permission-list')
]
