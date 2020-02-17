from django.urls import path 

from .views import product_create_view


app_name = 'products'


urlpatterns = [
	path('create/', product_create_view, name='create')
]



