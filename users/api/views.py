from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from ..models import User

# API VIEWS
class UserViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    def destroy(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
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