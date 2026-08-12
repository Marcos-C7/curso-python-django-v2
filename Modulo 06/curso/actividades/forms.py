from django import forms
from .models import Actividad


class ActividadForm(forms.ModelForm):
    class Meta:
        """
        El fomrulario no se va a encargar del campo 'usuario', ese se tomará
        en la vista usando al usuario logeado, por eso no lo ponemos en la 
        lista de `fields`.
        """
        model = Actividad
        fields = ("titulo", "descripcion", "fecha_inicio", "fecha_limite", "importancia", "estado")
        
        widgets = {
            "titulo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título",
            }),

            "descripcion": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Descripción",
            }),

            "fecha_inicio": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
                format="%Y-%m-%d",
            ),

            "fecha_limite": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
                format="%Y-%m-%d",
            ),
            
            # Como los campos `importancia` y `estado` son `ForeignKey` en el modelo, la clase `ModelForm` ya sabe
            # como procesarlos para la plantilla HTML mediante un <select>
            "importancia": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "estado": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }
