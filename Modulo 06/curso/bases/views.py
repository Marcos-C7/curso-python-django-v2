from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
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


class VistaPlantilla(View):
    plantilla = None
    contexto_extra = None

    def get(self, request):
        return render(request, self.plantilla, self.contexto_extra)

    def post(self, request):
        contexto = {'datos':request.POST}
        contexto.update(self.contexto_extra)

        return render(request, self.plantilla, contexto)


class MiPlantilla(VistaPlantilla):
    plantilla = 'bases/index.html'
    contexto_extra = {'tarjetas':range(1, 8)}


class VistaProducto(VistaPlantilla):
    plantilla = 'bases/index_2.html'
    contexto_extra = {'producto': 'Agua', 'precio': 10, 'cantidad': 2}


class VistaPlantillaDjango(TemplateView):
    template_name = 'bases/index.html'
    extra_context = {'tarjetas':range(1, 11)}

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        if self.request.method == 'POST':
            contexto['datos'] = self.request.POST

        return contexto
    
    def post(self, request):
        contexto = self.get_context_data()

        return render(request, self.template_name, contexto)


