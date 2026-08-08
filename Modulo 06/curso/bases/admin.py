from django.contrib import admin

from . import models


# Configuración del modelo Tarea para el panel de administrador
class TareaAdmin(admin.ModelAdmin):
    """ Esta clase describe como se administra el modelo en el Admin-site,
    que básicamente se compone de una lista de objetos y un formulario de 
    edición.
    """
    # Columnas a mostrar en la tabla
    list_display = ('titulo', 'fecha_inicio', 'fecha_limite', 'fecha_creacion')
    # Campos visibles pero no editables
    readonly_fields = ('fecha_creacion', )
    # Orden jerárquico de las columnas en la tabla. Usar '-' para invertir el orden.
    ordering = ('-fecha_creacion',)
    # Filtros laterales
    list_filter = ("fecha_inicio",)
    # Campos del modelo para el cuadro de búsqueda
    search_fields = ("titulo", "descripcion",)

admin.site.register(models.Tarea, TareaAdmin)