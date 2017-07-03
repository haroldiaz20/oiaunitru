from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'latest_question_list': ['hola', 'bienvenido']}
    return render(request, 'website/index.html', context)

def nosotros(request):
	return HttpResponse("Hola, Nosotros")
	
def contacto(request):
	return HttpResponse("Hola, Cpntacto")