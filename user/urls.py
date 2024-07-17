from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
app_name = 'user'

urlpatterns = [
    path('login/',auth_view.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('signup/',views.signup,name = 'signup'),
    path('logout/',views.logout_view, name = 'logout'),
]