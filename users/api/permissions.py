from rest_framework import permissions

from rest_framework.authtoken.models import Token

"""class IsOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated:
            acess_token = request.headers.get('Authorization')
            token = Token.objects.get(user=user)

            if acess_token == token:
                return True
            return False
        return False"""