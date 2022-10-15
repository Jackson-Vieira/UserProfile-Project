from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'users'

urlpatterns = [
    path('users/', views.index, name='index'),
    path('auth/register/', views.register, name='register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('users/<uuid:id>/', views.user, name='user'),
]