from django.shortcuts import render

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
    return render(request, 'login.html', {})