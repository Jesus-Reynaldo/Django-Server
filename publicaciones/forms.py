from django import forms
from .models import Publicacion
from django.forms.widgets import ClearableFileInput
class PublicacionForm(forms.ModelForm):
  class Meta:
    model = Publicacion
    fields =['title', 'description', 'image_file']
    widgets = {
      'image_file': ClearableFileInput(attrs={'multiple': True,'id': 'id_imagen'}),
    }
    