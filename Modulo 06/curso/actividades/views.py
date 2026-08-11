from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ActividadForm
from .models import Actividad

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

    def get_queryset(self):
        objetos = Actividad.objects.filter(usuario=self.request.user)

        return objetos

