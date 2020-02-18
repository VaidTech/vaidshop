from django.urls import path 

app_name = 'shops'

from .views import (
	shop_create_view,
	shop_list_view,
	shop_update_view,
	shop_detail_view,
	shop_delete_view,
	shop_product_list_view,
	)


urlpatterns = [
	path('create/', shop_create_view, name='create'),
	path('update/<int:id>/', shop_update_view, name='update'),
	path('list/', shop_list_view, name='list'),
	path('detail/<int:id>/', shop_detail_view, name='detail'),
	path('delete/<int:id>/', shop_delete_view, name='delete'),
	path('products/<int:id>/', shop_product_list_view, name='shop-products')
]



