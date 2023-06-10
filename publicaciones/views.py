from django.shortcuts import render, redirect
from .models import Publicacion 
from .forms import PublicacionForm

def index(request):
  publicaciones=Publicacion.objects.all()
  context={
    'publicaciones':publicaciones
  }
  return render(request, 'index.html', context)

def create_post(request):
  if request.method == 'POST':
    form = PublicacionForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
      return redirect('index')
  else:
    form = PublicacionForm()
  return render(request, 'create_post.html', {'form': form})