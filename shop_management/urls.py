from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


urlpatterns = [
	path("", RedirectView.as_view(url="/accounts/dashboard/")),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('employee/', include('employees.urls')),
    path('shops/', include('shops.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls'))
]



if settings.DEBUG:
    urlpatterns += \
        static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += \
        static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    



