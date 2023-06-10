from django.db import models
from datetime import date
# Create your models here.
class Publicacion(models.Model):
  title = models.CharField(max_length=100)
  description= models.TextField()
  imagen= models.ImageField(upload_to='images/')
  date_created = models.DateTimeField(default=date.today())
  def __str__(self):
    return self.title