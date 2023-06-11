from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
class CustomUser(AbstractUser):
    # Agrega campos adicionales según tus necesidades
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    avatar=models.ImageField(upload_to='avatars/', null=True, blank=True)
    date_born = models.DateField(default=timezone.now)
    # Añade relaciones y campos adicionales según tus necesidades
    follows = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username
