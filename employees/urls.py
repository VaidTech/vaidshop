from django.urls import path 

from .views import employee_create_view, employee_list_view


app_name = 'employees'


urlpatterns = [
    path('create/', employee_create_view, name='create'),
    path('list/', employee_list_view, name='list')
]






