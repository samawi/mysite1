from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('signup', views.user_signup, name='user_signup'),
]