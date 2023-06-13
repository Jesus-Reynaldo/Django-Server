from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .forms import SignUpForm
from .models import CustomUser
from publicaciones.models import Publicacion
def user(request):
    return HttpResponse('<h1>User</h1>');

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Mostrar mensaje de error de inicio de sesión incorrecto
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirige a la página principal después del registro exitoso
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile_view(request, username):
    user_view = get_object_or_404(CustomUser, username=username)
    posts = Publicacion.objects.filter(user=user_view)
    context={
        'user_view': user_view,
        'posts': posts,
    }
    return render(request, 'profile.html', context)

@login_required
def follow_user(request, username):
    user = request.user
    followed_user = CustomUser.objects.get(username=username)
    user.follow(followed_user)
    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    user = request.user
    followed_user = CustomUser.objects.get(username=username)
    user.unfollow(followed_user)
    return redirect('profile', username=username)