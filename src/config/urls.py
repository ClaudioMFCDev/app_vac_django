
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as views_django

urlpatterns = [
    # si se accede a name y no al url, se evitan conflictos al cambiar la url
    path('admin/', admin.site.urls),
    path('', views.mi_pagina_inicio, name='inicio'),
    path('usuarios/lista/', views.lista_usuarios, name='lista_de_usuarios'),
    path('pacientes/lista/', views.lista_pacientes, name='lista_de_pacientes'),
    # path('login/', views.login, name='login'),
    # LoginView es una clase, por ende, LoginView.as_view indicamos que se comporte como una funcion
    path('login/', views_django.LoginView.as_view(template_name="login.html"), name='login'),
    
]
