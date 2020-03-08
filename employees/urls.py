from django.urls import path
from .views import(employee_create_view, employee_list_view, employee_update_view, 
	employee_delete_view, employee_detail_view)

app_name = 'employees'

urlpatterns = [
	path('list/', employee_list_view, name='list'),
    path('create/', employee_create_view, name='create'),
    path('update/<int:id>/', employee_update_view, name='update'),
    path('delete/<int:id>/', employee_delete_view, name='delete'),
    path('detail/<int:id>/', employee_detail_view, name='detail')
]
