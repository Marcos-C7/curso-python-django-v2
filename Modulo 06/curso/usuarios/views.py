from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import CrearUsuarioForm


class Registro(CreateView):
    template_name = "usuarios/registro.html"
    form_class = CrearUsuarioForm
    success_url = reverse_lazy('core:home')

