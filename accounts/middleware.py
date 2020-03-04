from django.utils.deprecation import MiddlewareMixin
from orders.models import Order 

from owners.models import Owner


class DashboardMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
        	user = request.user
        	if user.is_owner:
        		owner = Owner.objects.get(user=user)
        	else:
        		employee = user.employee
        		owner = employee.owner
        	order = Order.objects.filter(owner=owner)
        	request.order_count = order.count()
        



