from django.db import models
from datetime import date
from user.models import CustomUser
# Create your models here.
class Publicacion(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
  title = models.CharField(max_length=100)
  description= models.TextField()
  image_file = models.ImageField(upload_to='images/')
  date_created = models.DateTimeField(default=date.today())
  def __str__(self):
    return f"Post {self.pk}"