from django.urls import path 

from .views import owner_register_view, login_view, dashboard_view, logout_view, profile_view


app_name = 'accounts'


urlpatterns = [
    path('register/owner/', owner_register_view, name='owner-register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile')
]

