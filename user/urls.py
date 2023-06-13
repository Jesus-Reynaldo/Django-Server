from django.urls import path
from . import views

urlpatterns = [
  path('',views.user,name='user'),
  path('login/',views.login_view,name='login'),
  path('signup/',views.signup_view,name='signup'),
  path('logout/',views.logout_view,name='logout'),
  path('profile/<str:username>',views.profile_view,name='profile'),
  path('follows/<str:username>', views.follow_user, name='follow'),
  path('unfollow/<str:username>/', views.unfollow_user, name='unfollow')
]