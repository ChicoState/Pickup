from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view()),
    path('profile/', views.MyProfile.as_view(), name='profile'),
    path('register/', views.register),
    path('logout/', views.logout_user),
    path('postJson', views.postJson),
    path('upload/', views.upload),
]