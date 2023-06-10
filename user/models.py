from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Agrega campos adicionales según tus necesidades
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    # Añade relaciones y campos adicionales según tus necesidades
    follows = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username
