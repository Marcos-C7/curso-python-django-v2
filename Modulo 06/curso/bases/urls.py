from django.urls import path

from . import views

app_name = 'bases'
urlpatterns = [
    path('vista_funcion/', views.vista_funcion, name='vista_funcion')
]

