from django.contrib.auth import views as auth_views
from .forms import LoginForm

from django.urls import path
from . import views
app_name = 'cart'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('singup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='html/login.html', authentication_form = LoginForm), name='login'),
    path('logout/', views.user_logout, name='logout')
]