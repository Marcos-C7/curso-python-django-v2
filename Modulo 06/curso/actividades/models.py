from django.contrib.auth.models import User
from django.db import models
from django.utils import timesince


class Importancia(models.Model):
    titulo = models.CharField(max_length=32, null=False, verbose_name="título")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creación")

    def __str__(self):
        """ Es importante definir esto ya que esto se mostrará en los formularios """
        return self.titulo
    
    class Meta:
        # Configuración para el admin-site
        verbose_name = 'Etiqueta de importancia'
        verbose_name_plural = 'Etiquetas de importancia'


class Estado(models.Model):
    titulo = models.CharField(max_length=32, null=False, verbose_name="título")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creación")
    
    def __str__(self):
        """ Es importante definir esto ya que esto se mostrará en los formularios """
        return self.titulo
    
    class Meta:
        # Configuración para el admin-site
        verbose_name = 'Etiqueta de estado'
        verbose_name_plural = 'Etiquetas de estado'


class Actividad(models.Model):
    titulo = models.CharField(max_length=256, null=False, verbose_name="título")
    descripcion = models.TextField(verbose_name="descripción", null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField(verbose_name="fecha límite")
    importancia = models.ForeignKey(Importancia, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Empezar sin el usuario y luego explicar por qué hay que agregarlo
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="fecha actualización")

    def __str__(self):
        return self.titulo
    
    @property
    def time_since(self):
        return timesince.timesince(self.fecha_creacion)
    
    class Meta:
        # Configuración para el admin-site
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'


