from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def vista_funcion(request):
    return render(request, 'bases/base.html')

