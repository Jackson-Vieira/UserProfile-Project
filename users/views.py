from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from .forms import SignUpForm
from .models import User
from .serializers import UserSerializer

def index(request):
    users = User.objects.all()
    
    template_name = "users/index.html"
    context = {
        'users':users
    }
    return render(request, template_name=template_name, context=context)

def user(request, id):
    user = User.objects.get(pk=id)  
    context = {'user_info':user}
    template_name = 'users/user.html'
    return render(request, template_name=template_name, context=context)

def register(request):
    error_message = False
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()

            if request.user.is_anonymous == False:
                logout(request)

            username, password = request.POST['username'], request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user=user)
            return HttpResponseRedirect(reverse('users:user', args=[user.id,]))

        error_message = "ERROR!"

    template_name = 'users/register.html'

    context = {
        'form':form,
        'error_message':error_message,
    }

    return render(request, template_name, context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:register"))

# API VIEWS
class UserViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    def destroy(self, request, *args, **kwargs):
        user = request.user
        pk = self.kwargs.get('pk')
        if (str(user.id) == pk):
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    def update(self, request, *args, **kwargs):
        user = request.user
        pk = self.kwargs.get('pk')
        if (str(user.id) == pk):
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    queryset = User.objects.all()
    serializer_class = UserSerializer