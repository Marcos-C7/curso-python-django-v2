from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import pdb


# Create your views here.
def vista_funcion(request):
    if request.method == 'GET':
        return render(request, 'bases/index.html', {'tarjetas':range(1, 8)})
    elif request.method == 'POST':
        return render(request, 'bases/index.html', {'tarjetas':range(1, 8), 'datos':request.POST})


class VistaClase(View):
    def get(self, request):
        return render(request, 'bases/index.html', {'tarjetas':range(1, 8)})

    def post(self, request):
        return render(request, 'bases/index.html', {'tarjetas':range(1, 8), 'datos':request.POST})

