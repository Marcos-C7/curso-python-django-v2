from django.urls import path

from . import views

app_name = 'bases'
urlpatterns = [
    path('vista_funcion/', views.vista_funcion, name='vista_funcion'),
    path('vista_clase/', views.VistaClase.as_view(), name='vista_clase'),
]

