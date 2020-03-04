from django.urls import path 

from .views import (
	attendence_add_view, 
	attendence_list, 
	attendence_list_detail,
	attendence_edit_view,
	attendence_delete_view,
)


app_name = 'attendences'


urlpatterns = [
	path('add/', attendence_add_view, name='attendence-add'),
	path('edit/<int:id>/', attendence_edit_view, name='attendence-edit'),
	path('delete/<int:id>/', attendence_delete_view, name='attendence-delete'),
	path('list/', attendence_list, name='attendence-list'),
	path('list/detail/<int:employee_id>/', attendence_list_detail, name='attendence-list-detail')
]



