from django.urls import path 
from .views import order_confirm_view, order_list_view, order_delete_view, order_product_view,order_confirm_update_view, order_product_update_view

app_name = 'orders'


urlpatterns = [
	path("create/", order_confirm_view, name="create"),
	path('list/', order_list_view, name="list"),
	path('delete/<int:id>/', order_delete_view, name="delete"),
	path('order-product/<int:id>/', order_product_view, name='order-product'),
	path('update/<int:id>/', order_confirm_update_view, name='update'),
	path('order-product/update/<int:id>/', order_product_update_view, name='order-product-update'),
]