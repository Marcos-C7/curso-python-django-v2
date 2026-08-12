from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, TemplateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ActividadForm
from .models import Actividad, Estado, Importancia

import lorem
import datetime
import random

# Create your views here.
class Nueva(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/nueva.html'
    form_class = ActividadForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        return super().form_valid(form)


class Lista(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/lista.html'
    context_object_name = 'actividades'
    paginate_by = 5

    def get_queryset(self):
        objetos = Actividad.objects.filter(usuario=self.request.user)

        return objetos


class Generador(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/generador.html'

    def post(self, request):
        # Número de actividades indicadas en el formulario
        cantidad = request.POST.get('cantidad', '0')
        
        if not cantidad or not cantidad.isdigit():
            cantidad = '0'
        
        cantidad = int(cantidad)

        # Fecha mínima de inicio de las actividades
        fecha_base = datetime.date(year=2023, month=1, day=1)
        # Lista de etiquetas existentes
        et_importancia = Importancia.objects.all()
        et_estado = Estado.objects.all()

        for _ in range(cantidad):
            actividad = Actividad()
            actividad.titulo = lorem.sentence()
            actividad.descripcion = lorem.paragraph()
            # Fecha de inicio aleatorio entre 0 y 100 días después de la fecha base
            actividad.fecha_inicio = fecha_base + datetime.timedelta(days=random.randint(0, 100))
            # Fecha límite aleatorio entre 30 y 90 días después de la fecha de inicio
            actividad.fecha_limite = actividad.fecha_inicio + datetime.timedelta(days=random.randint(30, 90))
            # Asignamos la actividad al usario autenticado
            actividad.usuario = request.user
            # Importancia y estado aleatorio
            actividad.importancia = et_importancia[random.randint(0, len(et_importancia) - 1)]
            actividad.estado = et_estado[random.randint(0, len(et_estado) - 1)]
            
            actividad.save()

        # Redireccionamos a la lista de actividades
        return redirect('actividades:lista')


class Detalle(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/detalle.html'
    
    def get_queryset(self):
        objetos = Actividad.objects.filter(usuario=self.request.user)

        return objetos


class Editar(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/nueva.html'
    form_class = ActividadForm
    
    def get_queryset(self):
        objetos = Actividad.objects.filter(usuario=self.request.user)

        return objetos

    def get_success_url(self):
        return reverse('actividades:detalle', args=(self.kwargs['pk'],))


class Eliminar(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    template_name = 'actividades/detalle.html'
    extra_context = {'confirmar_eliminar': True}
    success_url = reverse_lazy('core:home')
    
    def get_queryset(self):
        objetos = Actividad.objects.filter(usuario=self.request.user)

        return objetos

