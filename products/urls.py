from django.urls import path 

from .views import product_create_view, product_detail_view


app_name = 'products'


urlpatterns = [
	path('create/', product_create_view, name='create'),
	path('detail/<int:id>/', product_detail_view, name='detail')
]



