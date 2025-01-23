from django.http import HttpResponse

def saludo(request):  # primera vista
    return HttpResponse("Saludando..")

def inicio(request):  # primera vista
    return HttpResponse("Inicio..")

def despedida(request):  # primera vista
    return HttpResponse("Adiós..")