from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
import uuid

LOCATION_CHOICES = [
    ('United states','United States'),
    ('Brazil','Brazil'),
]

class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        unique=True,
        editable=False,
        null=False, 
        blank=False,
        )

    birth_date = models.DateField(
        'birth date',
        null=False,
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