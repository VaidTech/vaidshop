from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model



User = get_user_model()

class DashboardMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        request.owner = 's'
        print(request.owner)



