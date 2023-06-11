from django.shortcuts import render, redirect
from .models import Publicacion 
from .forms import PublicacionForm

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_authenticated:
        # Obtener las publicaciones del usuario actual
        publicaciones_usuario = Publicacion.objects.filter(user=request.user)

        # Obtener las publicaciones de los usuarios que el usuario actual está siguiendo
        usuarios_follows = request.user.follows.all()
        publicaciones_follows = Publicacion.objects.filter(user__in=usuarios_follows)

        # Concatenar las publicaciones del usuario actual y las publicaciones de los seguidos
        publicaciones = publicaciones_usuario | publicaciones_follows
    else:
        # Si el usuario no está autenticado, solo mostrar todas las publicaciones
        publicaciones = Publicacion.objects.all()

    context = {'publicaciones': publicaciones}
    return render(request, 'index.html', context)

def create_post(request):
  if request.method == 'POST':
    form = PublicacionForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user
      post.save()
      return redirect('index')
  else:
    form = PublicacionForm()
  return render(request, 'create_post.html', {'form': form})