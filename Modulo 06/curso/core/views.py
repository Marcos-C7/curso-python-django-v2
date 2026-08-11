from django.shortcuts import render
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginRequiredMixin, RedirectView):
    login_url = reverse_lazy('usuarios:iniciar_sesion')
    pattern_name = 'actividades:lista'

