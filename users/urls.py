from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('users/', views.index, name='index'),
    path('users/register/', views.register, name='register'),
    path('users/logout/', views.logout_user, name='logout'),
    path('users/<uuid:id>', views.user, name='user'),
]

