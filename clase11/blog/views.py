from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mostrar_post(request):
    return HttpResponse("Van todos los posts del blog")

def mostrar_comments(request):
    return HttpResponse("Van todos los comentarios del blog")