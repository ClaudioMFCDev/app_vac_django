from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django

def mi_pagina_inicio(request):
    usuarios = [
        {"nombre": 'Claudio', "apellido": 'Castillo'},
        {"nombre": 'Marcelo', "apellido": 'Romero'},
        {"nombre": 'Fabian', "apellido": 'Ramirez'},
          ]
    contexto = {'todos_los_usuarios': usuarios}
    
    # return render(request, 'template_name', contexto)    
    return render(request, 'mi_pagina_inicio.html', contexto)
  
def lista_usuarios(request):
    return render(request, 'lista_usuarios.html', {})


def lista_pacientes(request):
    return render(request, 'lista_pacientes.html', {})

def login(request):
    # string("dasdasdas")
    
    se_autentico = False
    salio_mal = True
    username = ""
    if request.method == "POST":
        username = request.POST.get("username", default=None)
        password = request.POST.get("password", default=None)
        usuario = authenticate(request, username=username, password=password)    
        # print("usuario get -->", usuario)
        se_autentico = True
        
        if usuario:
            salio_mal = False
            login_django(request, usuario)
            return redirect("inicio")
            
    ctx = {
        "se_autentico": se_autentico,
        "salio_mal": salio_mal,
        "username": username,
    }
    
    return render(request, 'login.html', {})