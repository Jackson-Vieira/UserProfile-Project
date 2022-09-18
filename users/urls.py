
from django.urls import path
from django.contrib.auth.views import LoginView


from . import views


app_name = 'users'

urlpatterns = [
    path('users/', views.index, name='index'),
    path('users/register/', views.register, name='register'),
    path('users/logout/', views.logout_user, name='logout'),
    path('users/login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('users/<uuid:id>', views.user, name='user'),
]