from django.urls import path

from . import views

app_name = 'bases'
urlpatterns = [
    path('vista_funcion/', views.vista_funcion, name='vista_funcion'),
    path('vista_clase/', views.VistaClase.as_view(), name='vista_clase'),
    path('vista_plantilla/', views.MiPlantilla.as_view(), name='vista_plantilla'),
    path('vista_producto/', views.VistaProducto.as_view(), name='vista_producto'),
    path('vista_plantilla_django/', views.VistaPlantillaDjango.as_view(), name='vista_plantilla_django'),
]

