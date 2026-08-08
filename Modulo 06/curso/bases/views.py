from django.shortcuts import render
from django.http import HttpResponse
import pdb


# Create your views here.
def vista_funcion(request):
    if request.method == 'GET':
        return render(request, 'bases/index.html', {'tarjetas':range(1, 8)})
    elif request.method == 'POST':
        return render(request, 'bases/index.html', {'tarjetas':range(1, 8), 'datos':request.POST})

