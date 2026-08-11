from django.urls import path

from . import views

app_name = 'actividades'
urlpatterns = [
    path('nueva/', views.Nueva.as_view(), name='nueva'),
    path('lista/', views.Lista.as_view(), name='lista'),
    path('generador/', views.Generador.as_view(), name='generador'),
    path('detalle/<int:pk>/', views.Detalle.as_view(), name="detalle"),
]

