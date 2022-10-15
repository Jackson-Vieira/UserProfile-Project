from ast import arg
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

import uuid

LOCATION_CHOICES = [
    ('United states','United States'),
    ('Brazil','Brazil'),
]


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        editable=False,
        null=False, 
        blank=False,
        )

    birth_date = models.DateField(
        'birth date',
        null=True,
        blank=False,
    )

    location = models.TextField(
        'location',
        choices=LOCATION_CHOICES,
        blank=True,
        null=True,
    )

    perfil_photo = models.ImageField(
        'perfil photo',
        upload_to='users',
        blank=True,
        null = True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['date_joined']

    def save(self, *args, **kwargs):
        print("?")
        super().save(*args, **kwargs)
        Token.objects.get_or_create(user=self)