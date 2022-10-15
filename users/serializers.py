from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserSerializer(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()

    class Meta:
        model = User   
        fields = ['id', 'username', 'perfil_photo', 'location', 'birth_date', 'last_login', 'date_joined', 'token',]
        read_only_fields = ['last_login', 'date_joined']
        extra_kwargs = {'password': {'write_only': True},}

    def get_token(self, obj):
        return Token.objects.get(user=obj).key