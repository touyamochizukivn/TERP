from django.urls import path
from django.contrib.auth.views import LogoutView

from authentication.views import LoginView
from authentication.forms import LoginForm

urlpatterns = [
    path('login', LoginView.as_view(redirect_authenticated_user=True, template_name='auth/login.html', authentication_form=LoginForm), name='login'),
    path('logout', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]
