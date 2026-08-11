from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy

from .forms import CrearUsuarioForm, IniciarSesionForm, CambiarPasswordForm


class Registro(CreateView):
    template_name = "usuarios/registro.html"
    form_class = CrearUsuarioForm
    success_url = reverse_lazy('usuarios:iniciar_sesion')


class IniciarSesion(LoginView):
    template_name = "usuarios/iniciar_sesion.html"
    authentication_form = IniciarSesionForm
    next_page = reverse_lazy('core:home')


class CerrarSesion(LogoutView):
    """
    Para que la vista cierre la sesión, debe de ser mediante método POST
    """
    next_page = reverse_lazy('usuarios:iniciar_sesion')


class CambiarPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    form_class = CambiarPasswordForm
    success_url = reverse_lazy('core:home')


