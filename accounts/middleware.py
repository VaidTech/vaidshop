from django.utils.deprecation import MiddlewareMixin
from orders.models import Order 



class DashboardMiddleWare(MiddlewareMixin):
    def process_request(self, request):
    	if request.user.is_authenticated:
        	order = Order.objects.filter(user=request.user)
        	request.order_count = order.count()
        



